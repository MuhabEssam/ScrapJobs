import scrapy

class JobListingSpider(scrapy.Spider):
    name = 'job_listing'
    start_urls = ['https://www.indeed.com/jobs?q=python+developer']

    def parse(self, response):
        for job in response.css('div.jobsearch-SerpJobCard'):
            yield {
                'title': job.css('h2.title a::text').get(),
                'company': job.css('span.company::text').get(),
                'location': job.css('span.location::text').get(),
                'summary': job.css('div.summary::text').get(),
            }

        next_page = response.css('a.pagination-next::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
