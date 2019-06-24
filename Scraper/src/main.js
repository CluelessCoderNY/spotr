const puppeteer = require("puppeteer")

const main = async () => {
  const postUrl =
    "https://newyork.craigslist.org/mnh/rvs/d/brooklyn-double-cozy-bed-pleasure-way/6918858716.html";

  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  await page.goto(postUrl, { waitUntil: "networkidle2" });

  const data = await page.evaluate(() => {
    const title = document.querySelector('span[id="titletextonly"]').innerText;
    const price = document.querySelector('span[class="price"]').innerText;
    const description = document.querySelector('section[id="postingbody"]')
      .innerText;

    return {
      title,
      price,
      description
    };
  });

  console.log(data);

  debugger;

  await browser.close();
}

main()

