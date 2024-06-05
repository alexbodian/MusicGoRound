const playwright = require('playwright');
const fs = require('fs').promises; // Use fs.promises for async/await support

(async () => {
  // Launch the browser
  const browser = await playwright.chromium.launch();
  const context = await browser.newContext();
  const page = await context.newPage();

  // Navigate to the webpage
  await page.goto('https://www.musicgoround.com/products/GUEL/electric-guitars?sortBy=xp.Price&page=1',{ waitUntil: 'networkidle'});

  // Get the HTML of the current page
  const htmlContent = await page.content();

  // Output the HTML to a file named 'page.html'
  await fs.writeFile('page.html', htmlContent);


  // Take a screenshot and save it as 'screenshot.png'
  await page.screenshot({ path: 'screenshot.png', fullPage: true });

  // Close the browser
  await browser.close();
})();









/*
// Define some async functions
async function asyncFunction1() {
    // Simulate some asynchronous work with a timeout
    await new Promise(resolve => setTimeout(resolve, 1000));
    console.log('Async Function 1 is done!');
  }
  
  async function asyncFunction2() {
    // Simulate some asynchronous work with a timeout
    await new Promise(resolve => setTimeout(resolve, 1000));
    console.log('Async Function 2 is done!');
  }
  
  async function asyncFunction3() {
    // Simulate some asynchronous work with a timeout
    await new Promise(resolve => setTimeout(resolve, 1000));
    console.log('Async Function 3 is done!');
  }
  
  // Run the async functions synchronously
  (async () => {
    await asyncFunction1(); // Wait for asyncFunction1 to finish
    await asyncFunction2(); // Wait for asyncFunction2 to finish
    await asyncFunction3(); // Wait for asyncFunction3 to finish
  })();
*/  