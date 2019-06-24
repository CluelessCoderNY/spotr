const puppeteer = require("puppeteer");

const main = async () => {
  const postUrl =
    "https://hudsonvalley.craigslist.org/rvs/d/stormville-winnebago-view-diesel/6918806587.html";

  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();

  await page.goto(postUrl, { waitUntil: "networkidle2" });

  const data = await page.evaluate(() => {
    clickButton = async () => {
      // await document.querySelector('button[class="reply-button').click();
      // await page.waitFor(10000);
    };

    const title = document.querySelector('span[id="titletextonly"]').innerText;
    const price = document.querySelector('span[class="price"]').innerText;
    const description = document.querySelector('section[id="postingbody"]')
      .innerText;
    const postAge = document.querySelector('time[class="date timeago"]')
      .innerText;

    const rawTags = document.querySelectorAll('p[class="attrgroup"] span');
    const convertedTags = Array.prototype.slice.call(rawTags);
    const tags = convertedTags.map(tag => tag.innerText);

    const nodes = document.querySelector('div[id="thumbs"]').childNodes;
    const convertedNodes = Array.prototype.slice.call(nodes);
    const images = convertedNodes.map(node => node.getAttribute("href"));

    return {
      title,
      price,
      description,
      postAge,
      tags,
      images
    };
  });

  console.log(data);

  debugger;

  await browser.close();
};

main();
