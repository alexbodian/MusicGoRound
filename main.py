import asyncio
from playwright.async_api import async_playwright

base_url = 'https://www.musicgoround.com/'
electric_guitars_page1 = "https://www.musicgoround.com/products/GUEL/electric-guitars?sortBy=xp.Price&page=1"


async def getNumberOfPages(base_page):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(base_page)
        await page.wait_for_selector('.page-link')
        await page.screenshot(path='screenshot.png',)

        elements = await page.query_selector_all('.page-link')
        total_pages = await elements[len(elements)-2].inner_text()
        await browser.close()
        return total_pages

        # print(await element.inner_text())


async def pullMetadata(base_page):
    '''
    CSS Classes for metadata

    Name
    card-title

    Price
    card-text--price

    Link to Item
    d-flex flex-fill 

    '''

    async with async_playwright() as p:
        list_of_items = []
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(base_page)
        await page.wait_for_selector('.page-link')

        title_elems = await page.query_selector_all('.card-title')
        price_elems = await page.query_selector_all('.card-text--price')
        link_elems = await page.query_selector_all('.text-decoration-none')

        # print(await i.get_attribute('href'))

        for x in range(0, len(title_elems)):
            list_of_items.append(
                {
                    'title': await title_elems[x].inner_text(),
                    'price': await price_elems[x].inner_text(),
                    'url': base_url + await link_elems[x].get_attribute('href')



                }


            )

        await browser.close()
        return list_of_items


async def run_async_functions():

    # Create a list to store the tasks
    tasks = []
    # print(story_details_json[0]['ID'])

    # task = asyncio.create_task(getNumberOfPages(electric_guitars_page1))
    # tasks.append(task)
    # await asyncio.gather(*tasks)

    # totalPages = await tasks[0]
    # print(totalPages)

    task = asyncio.create_task(pullMetadata(electric_guitars_page1))
    tasks.append(task)
    await asyncio.gather(*tasks)
    res = await tasks[0]
    print(res)

    '''
    for x in story_details_json :
    task = asyncio.create_task(save_story_to_pdf(x))
    tasks.append(task)
    # print(count)
    if count == 1:
        await asyncio.gather(*tasks)
        count = 0
    else:
        count += 1

    step+=1
    if step == 1000:
        break
        
    

    results = []
    # # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    # Retrieve the results from the tasks
    index_for_story_details_json = 0
    for task in tasks:
        result = await task




    count = 1
    step = 1
    # for x in dateRangePages:
    for x in story_details_json:
        task = asyncio.create_task((x))
        tasks.append(task)
        # print(count)
        if count == 1:
            await asyncio.gather(*tasks)
            count = 0
        else:
            count += 1

        step += 1
        if step == 1000:
            break

    results = []
    # # Wait for all tasks to complete
    await asyncio.gather(*tasks)

    '''

asyncio.run(run_async_functions())
