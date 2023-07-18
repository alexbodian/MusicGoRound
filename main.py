import asyncio
from playwright.async_api import async_playwright


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()


async def run_async_functions():

    # Create a list to store the tasks
    tasks = []
    # print(story_details_json[0]['ID'])

    # Should be able to get the name and author since that info
    # is in the json for story details

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


asyncio.run(run_async_functions())
