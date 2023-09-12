import asyncio
from datetime import date, timedelta

import uvicorn
import uvloop
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from pytz import timezone
from loguru import logger

from crawler import session_scope
from crawler.common.enums import CampaignType
from crawler.common.factory import CampaignTypeClient
from crawler.common.models import Profile, User
from crawler.common.tasks.profile import crawl_profiles

from crawler.brands.views import router as sb_router
from crawler.brands.tasks.campaign import crawl_campaigns as sb_crawl_campaigns
from crawler.brands.tasks.ad_group import crawl_ad_groups as sb_crawl_ad_groups
from crawler.brands.tasks.keyword import crawl_keywords as sb_crawl_keywords
from crawler.brands.tasks.neg_keyword import crawl_neg_keywords as sb_crawl_neg_keywords
from crawler.brands.tasks.keyword_report import crawl_keyword_report as sb_crawl_keyword_report
from crawler.brands.tasks.target_report import crawl_target_report as sb_crawl_target_report
from crawler.brands.tasks.keyword_report import crawl_keyword_report_creative as sb_crawl_keyword_report_creative
from crawler.brands.tasks.target_report import crawl_target_report_creative as sb_crawl_target_report_creative

from crawler.display.views import router as sd_router
from crawler.display.tasks.campaign import crawl_campaigns as sd_crawl_campaigns
from crawler.display.tasks.ad_group import crawl_ad_groups as sd_crawl_ad_groups
from crawler.display.tasks.product_ad import crawl_product_ads as sd_crawl_product_ads
from crawler.display.tasks.target import crawl_targets as sd_crawl_targets
from crawler.display.tasks.neg_target import crawl_neg_targets as sd_crawl_neg_targets
from crawler.display.tasks.target_report import crawl_target_report as sd_crawl_target_report
from crawler.display.tasks.product_ad_report import crawl_product_ad_report as sd_crawl_product_ad_report

from crawler.products.views import router as sp_router
from crawler.products.tasks.campaign import crawl_campaigns as sp_crawl_campaigns
from crawler.products.tasks.ad_group import crawl_ad_groups as sp_crawl_ad_groups
from crawler.products.tasks.product_ad import crawl_product_ads as sp_crawl_product_ads
from crawler.products.tasks.keyword import crawl_keywords as sp_crawl_keywords
from crawler.products.tasks.neg_keyword import crawl_neg_keywords as sp_crawl_neg_keywords
from crawler.products.tasks.camp_neg_keyword import crawl_camp_neg_keywords as sp_crawl_camp_neg_keywords
from crawler.products.tasks.target import crawl_targets as sp_crawl_targets
from crawler.products.tasks.neg_target import crawl_targets as sp_crawl_neg_targets
from crawler.products.tasks.keyword_report import crawl_keyword_report as sp_crawl_keyword_report
from crawler.products.tasks.target_report import crawl_target_report as sp_crawl_target_report
from crawler.products.tasks.product_ad_report import crawl_product_ad_report as sp_crawl_product_ad_report

app = FastAPI()
app.include_router(sd_router, prefix='/api/v1')
app.include_router(sb_router, prefix='/api/v1')
app.include_router(sp_router, prefix='/api/v1')


async def start_up_event():
    '''
    loop = asyncio.get_running_loop()

    # Crawls Profiles
    await crawl_profiles()

    sb_client = await CampaignTypeClient.create(loop, CampaignType.SB)
    sd_client = await CampaignTypeClient.create(loop, CampaignType.SD)
    sp_client = await CampaignTypeClient.create(loop, CampaignType.SP)
    report_date = (date.today() - timedelta(days=3)).strftime('%Y%m%d')
    with session_scope() as session:
        profiles = session.query(Profile).all()
        for profile in profiles:
            # Crawls Campaigns
            await asyncio.gather(
                sb_crawl_campaigns(sb_client, profile.id),
                sd_crawl_campaigns(sd_client, profile.id),
                sp_crawl_campaigns(sp_client, profile.id)
            )
            # Crawls AdGroups
            await asyncio.gather(
                sb_crawl_ad_groups(sb_client, profile.id),
                sd_crawl_ad_groups(sd_client, profile.id),
                sp_crawl_ad_groups(sp_client, profile.id)
            )
            # Crawls the rest
            await asyncio.gather(
                sb_crawl_keywords(sb_client, profile.id),
                sb_crawl_neg_keywords(sb_client, profile.id),
                sb_crawl_keyword_report(sb_client, profile.id, report_date),
                sb_crawl_target_report(sb_client, profile.id, report_date),
                sb_crawl_keyword_report_creative(sb_client, profile.id, report_date),  #newly created
                sb_crawl_target_report_creative(sb_client, profile.id, report_date),  #newly created

                sd_crawl_product_ads(sd_client, profile.id),
                sd_crawl_targets(sd_client, profile.id),
                sd_crawl_neg_targets(sd_client, profile.id),
                sd_crawl_product_ad_report(sd_client, profile.id, report_date),
                sd_crawl_target_report(sd_client, profile.id, report_date),

                sp_crawl_product_ads(sp_client, profile.id),
                sp_crawl_keywords(sp_client, profile.id),
                sp_crawl_neg_keywords(sp_client, profile.id),
                sp_crawl_camp_neg_keywords(sp_client, profile.id),
                sp_crawl_targets(sp_client, profile.id),
                sp_crawl_neg_targets(sp_client, profile.id),
                sp_crawl_product_ad_report(sp_client, profile.id, report_date),
                sp_crawl_keyword_report(sp_client, profile.id, report_date),
                sp_crawl_target_report(sp_client, profile.id, report_date)
            )
    '''

    loop = asyncio.get_running_loop()
    #sb_client = await CampaignTypeClient.create(loop, CampaignType.SB)
    #sd_client = await CampaignTypeClient.create(loop, CampaignType.SD)
    #sp_client = await CampaignTypeClient.create(loop, CampaignType.SP)
    report_date = (date.today() - timedelta(days=3)).strftime('%Y%m%d')
    with session_scope() as session:
        users_temp = session.query(User).filter_by(crawled_60d=False)
        users = users_temp.all()
        for user in users:
            '''
            # Crawls Profiles
            await crawl_profiles(user.refresh_token)
            '''
            for profile in user.profiles:
                try:
                    sb_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SB)
                    sd_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SD)
                    sp_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SP)
                except:
                    await asyncio.sleep(600)
                    sb_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SB)
                    sd_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SD)
                    sp_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SP)
                    try:
                        await asyncio.sleep(1200)
                        sb_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SB)
                        sd_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SD)
                        sp_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SP)
                    except Exception as e:
                        logger.error(f'1d Token Error: {e}')
                        continue

                logger.info("**********!")
                logger.info(profile.id)
                logger.info("**********!")
                try:
                    # Crawls Campaigns
                    await asyncio.gather(
                        sb_crawl_campaigns(sb_client, profile.id),
                        sd_crawl_campaigns(sd_client, profile.id),
                        sp_crawl_campaigns(sp_client, profile.id)
                    )
                    # Crawls AdGroups
                    await asyncio.gather(
                        sb_crawl_ad_groups(sb_client, profile.id),
                        sd_crawl_ad_groups(sd_client, profile.id),
                        sp_crawl_ad_groups(sp_client, profile.id)
                    )
                    # Crawls the rest
                    await asyncio.gather(
                        sb_crawl_keywords(sb_client, profile.id),
                        sb_crawl_neg_keywords(sb_client, profile.id),
                        sb_crawl_keyword_report(sb_client, profile.id, report_date),
                        sb_crawl_target_report(sb_client, profile.id, report_date),
                        sb_crawl_keyword_report_creative(sb_client, profile.id, report_date),  #newly created
                        sb_crawl_target_report_creative(sb_client, profile.id, report_date),  #newly created

                        sd_crawl_product_ads(sd_client, profile.id),
                        sd_crawl_targets(sd_client, profile.id),
                        sd_crawl_neg_targets(sd_client, profile.id),
                        sd_crawl_product_ad_report(sd_client, profile.id, report_date),
                        sd_crawl_target_report(sd_client, profile.id, report_date),

                        sp_crawl_product_ads(sp_client, profile.id),
                        sp_crawl_keywords(sp_client, profile.id),
                        sp_crawl_neg_keywords(sp_client, profile.id),
                        sp_crawl_camp_neg_keywords(sp_client, profile.id),
                        sp_crawl_targets(sp_client, profile.id),
                        sp_crawl_neg_targets(sp_client, profile.id),
                        sp_crawl_product_ad_report(sp_client, profile.id, report_date),
                        sp_crawl_keyword_report(sp_client, profile.id, report_date),
                        sp_crawl_target_report(sp_client, profile.id, report_date)
                    )
                except:
                    await asyncio.sleep(300)
                    try:
                        # Crawls Campaigns
                        await asyncio.gather(
                            sb_crawl_campaigns(sb_client, profile.id),
                            sd_crawl_campaigns(sd_client, profile.id),
                            sp_crawl_campaigns(sp_client, profile.id)
                        )
                        # Crawls AdGroups
                        await asyncio.gather(
                            sb_crawl_ad_groups(sb_client, profile.id),
                            sd_crawl_ad_groups(sd_client, profile.id),
                            sp_crawl_ad_groups(sp_client, profile.id)
                        )
                        # Crawls the rest
                        await asyncio.gather(
                            sb_crawl_keywords(sb_client, profile.id),
                            sb_crawl_neg_keywords(sb_client, profile.id),
                            sb_crawl_keyword_report(sb_client, profile.id, report_date),
                            sb_crawl_target_report(sb_client, profile.id, report_date),
                            sb_crawl_keyword_report_creative(sb_client, profile.id, report_date),  #newly created
                            sb_crawl_target_report_creative(sb_client, profile.id, report_date),  #newly created

                            sd_crawl_product_ads(sd_client, profile.id),
                            sd_crawl_targets(sd_client, profile.id),
                            sd_crawl_neg_targets(sd_client, profile.id),
                            sd_crawl_product_ad_report(sd_client, profile.id, report_date),
                            sd_crawl_target_report(sd_client, profile.id, report_date),

                            sp_crawl_product_ads(sp_client, profile.id),
                            sp_crawl_keywords(sp_client, profile.id),
                            sp_crawl_neg_keywords(sp_client, profile.id),
                            sp_crawl_camp_neg_keywords(sp_client, profile.id),
                            sp_crawl_targets(sp_client, profile.id),
                            sp_crawl_neg_targets(sp_client, profile.id),
                            sp_crawl_product_ad_report(sp_client, profile.id, report_date),
                            sp_crawl_keyword_report(sp_client, profile.id, report_date),
                            sp_crawl_target_report(sp_client, profile.id, report_date)
                        )
                    except:
                        await asyncio.sleep(300)
                        try:
                            # Crawls Campaigns
                            await asyncio.gather(
                                sb_crawl_campaigns(sb_client, profile.id),
                                sd_crawl_campaigns(sd_client, profile.id),
                                sp_crawl_campaigns(sp_client, profile.id)
                            )
                            # Crawls AdGroups
                            await asyncio.gather(
                                sb_crawl_ad_groups(sb_client, profile.id),
                                sd_crawl_ad_groups(sd_client, profile.id),
                                sp_crawl_ad_groups(sp_client, profile.id)
                            )
                            # Crawls the rest
                            await asyncio.gather(
                                sb_crawl_keywords(sb_client, profile.id),
                                sb_crawl_neg_keywords(sb_client, profile.id),
                                sb_crawl_keyword_report(sb_client, profile.id, report_date),
                                sb_crawl_target_report(sb_client, profile.id, report_date),
                                sb_crawl_keyword_report_creative(sb_client, profile.id, report_date),  #newly created
                                sb_crawl_target_report_creative(sb_client, profile.id, report_date),  #newly created

                                sd_crawl_product_ads(sd_client, profile.id),
                                sd_crawl_targets(sd_client, profile.id),
                                sd_crawl_neg_targets(sd_client, profile.id),
                                sd_crawl_product_ad_report(sd_client, profile.id, report_date),
                                sd_crawl_target_report(sd_client, profile.id, report_date),

                                sp_crawl_product_ads(sp_client, profile.id),
                                sp_crawl_keywords(sp_client, profile.id),
                                sp_crawl_neg_keywords(sp_client, profile.id),
                                sp_crawl_camp_neg_keywords(sp_client, profile.id),
                                sp_crawl_targets(sp_client, profile.id),
                                sp_crawl_neg_targets(sp_client, profile.id),
                                sp_crawl_product_ad_report(sp_client, profile.id, report_date),
                                sp_crawl_keyword_report(sp_client, profile.id, report_date),
                                sp_crawl_target_report(sp_client, profile.id, report_date)
                            )
                        except Exception as e:
                            logger.error(f'1d Profile Error: {e}')
                            continue
        #users_temp.update({'crawled_60d': True})


async def crawl_60d():
    loop = asyncio.get_running_loop()
    #sb_client = await CampaignTypeClient.create(loop, CampaignType.SB)
    #sd_client = await CampaignTypeClient.create(loop, CampaignType.SD)
    #sp_client = await CampaignTypeClient.create(loop, CampaignType.SP)
    report_dates = [(date.today() - timedelta(days=i)).strftime('%Y%m%d') for i in range(60, 2, -1)]
    prod_ad_dates = [(date.today() - timedelta(days=i)).strftime('%Y%m%d') for i in range(6, 2, -1)]
    with session_scope() as session:
        users_temp = session.query(User).filter_by(crawled_60d=True)
        users = users_temp.all()
        for user in users:
            user.crawled_60d = False
            session.commit()
            for profile in user.profiles:
                profile.crawled_60d = False
                session.commit()
                try:
                    for report_date in report_dates:
                        try:
                            sb_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SB)
                            sd_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SD)
                            sp_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SP)
                        except:
                            await asyncio.sleep(600)
                            sb_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SB)
                            sd_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SD)
                            sp_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SP)
                            try:
                                await asyncio.sleep(1200)
                                sb_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SB)
                                sd_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SD)
                                sp_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SP)
                            except Exception as e:
                                logger.error(f'60d Token Error: {e}')
                                continue

                        try:
                            await asyncio.gather(
                                sb_crawl_keyword_report(sb_client, profile.id, report_date),
                                sb_crawl_keyword_report_creative(sb_client, profile.id, report_date),  #newly created
                                sb_crawl_target_report(sb_client, profile.id, report_date),  #newly created
                                sb_crawl_target_report_creative(sb_client, profile.id, report_date),  #newly created

                                sd_crawl_target_report(sd_client, profile.id, report_date),
                                #sd_crawl_product_ad_report(sd_client, profile.id, report_date),  #newly created

                                sp_crawl_target_report(sp_client, profile.id, report_date),
                                sp_crawl_keyword_report(sp_client, profile.id, report_date)
                                #sp_crawl_product_ad_report(sp_client, profile.id, report_date)
                            )
                            if (report_date == prod_ad_dates[0] or report_date == prod_ad_dates[1] or report_date == prod_ad_dates[2] or report_date == prod_ad_dates[3]):
                                await asyncio.gather(
                                    #sd_crawl_product_ad_report(sd_client, profile.id, report_date),  #newly created
                                    sp_crawl_product_ad_report(sp_client, profile.id, report_date)
                                )
                        except Exception as e:
                            logger.error(f'60d Report Date Error: {e}')
                            continue
                except Exception as e:
                    logger.error(f'60d Profile Error: {e}')
                    continue
            #user.crawled_60d = False
            logger.info("60d End User")
        #users.update({User.crawled_60d: False})
        #session.query(User).filter_by(crawled_60d=True).update({'crawled_60d': False})
        #users_temp.update({'crawled_60d': False})


async def tooth_event():
    loop = asyncio.get_running_loop()
    #sb_client = await CampaignTypeClient.create(loop, CampaignType.SB)
    #sd_client = await CampaignTypeClient.create(loop, CampaignType.SD)
    #sp_client = await CampaignTypeClient.create(loop, CampaignType.SP)
    report_dates = ['20211017', '20211018']#(date.today() - timedelta(days=3)).strftime('%Y%m%d')
    with session_scope() as session:
        users_temp = session.query(User).filter_by(id='144')
        users = users_temp.all()
        for user in users:
            sb_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SB)
            #sd_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SD)
            #sp_client = await CampaignTypeClient.create(user.refresh_token, loop, CampaignType.SP)
        profiles_temp = session.query(Profile).filter_by(id='2136836233403479')
        profiles = profiles_temp.all()
        for profile in profiles:
            logger.info("********************!")
            logger.info(profile.id)
            logger.info("********************!")

            for report_date in report_dates:
                # Crawls the rest
                await asyncio.gather(
                    sb_crawl_keyword_report(sb_client, profile.id, report_date),
                    #sb_crawl_target_report(sb_client, profile.id, report_date),

                    #sd_crawl_target_report(sd_client, profile.id, report_date),

                    #sp_crawl_keyword_report(sp_client, profile.id, report_date),
                    #sp_crawl_target_report(sp_client, profile.id, report_date)
                )


@app.on_event('startup')
async def main():
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop)
    # await start_up_event()
    scheduler = AsyncIOScheduler()
    '''
    scheduler.add_job(
        start_up_event,
        'interval',
        days=1,
        start_date='2021-01-01 11:00:00',
        timezone=timezone('Asia/Seoul'),
        jitter=120
    )

    scheduler.add_job(
        crawl_60d,
        'interval',
        days=1,
        start_date='2021-01-01 11:30:00',
        timezone=timezone('Asia/Seoul'),
        jitter=120
    )
    '''
    scheduler.add_job(
        tooth_event,
        'interval',
        days=1,
        start_date='2021-01-01 14:56:00',
        timezone=timezone('Asia/Seoul'),
        jitter=120
    )

    scheduler.start()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
