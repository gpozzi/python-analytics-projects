# Rocket launches, a best value anaylsis 🚀
Launching payloads, such as satellites or space station modules, into space is expensive and requires careful planning. Finding and investing in regions that have a developed space industry can reduce costs and improve the pace of space travel and exploration.

**The European Space Agency (ESA)** has decided to invest in countries that are home to the most efficient companies at sending payloads into space. In particular, they want to find countries with the **lowest average price per kilo** (across all companies for each country) that can launch **rockets** into **Low Earth Orbit (LEO)** according to each of their three classes (**light, medium, and heavy rockets**).

However, there are some additional contraints that the ESA has put in place for the selection process:

> Companies included in each country's average price must have a **Quality Assurance (QA) rating higher than 2**. QA is a rating based on previous launches. This constraint establishes a minimum level of performance for the selection process.

> Countries with a launch cost **under $10,000,000 in total** for all rocket launches across the three classes should be excluded. This constraint ensures that any selected countries will be able to manage the large volume of launches required.

To help you in your task, the ESA has made available to you three datasets: single-owner companies (datasets/SO-space.csv) and joint-ventures (datasets/JV-space.csv), both of which contain launch data on companies that offer space services. These are paired with the company info dataset (datasets/company_info.csv) which contains the company names, launch technology (rockets, balloons, planes, other), and their location details.

The launch classes are defined as follows based on their payload in Kilograms:
- Light <= 1,000
- 1,000 < Medium <= 10,000
- 10,000 < Heavy

## The data
### datasets/SO-space.csv - Space launch data for private single owner companies
> **Source**: SpaceFund
> **Company ID**: The company ID.
> **QA**: The quality assurance rating as given by an appointed third party agency.
> **Payload (kg)**: The weight in kilograms for the largest spacecraft launched by the company.
> **Launch Cost ($M)**: The launch cost for the largest spacecraft, in millions of USD.
> **Price ($/Kg)**: The price paid to hire the company services by a new client, in USD per kilogram.
> **Orbit Altitude**: The earth orbit achieved by the company's spacecraft.

### datasets/JV-space.csv - Space launch data for private joint-venture companies
> **Source**: SpaceFund
> **Company ID**: The company ID.
> **QA**: The quality assurance rating as given by an appointed third party agency.
> **Payload (tons)**: The weight in tons for the largest spacecraft launched by the company.
> **Launch Cost**: The launch cost for the largest spacecraft, in USD.
> **Price ($/ton)**: The price paid to hire the company services by a new client, in USD per ton.
> **Orbit Altitude**: The earth orbit achieved by the company's spacecraft.
### datasets/company_info.csv - Company name, launch technology, and geographical data
> **Source**: SpaceFund
> **ID**: The company ID.
> **Company**: The company name.
> **Tech Type**: The spacecraft type. Rocket, Spaceplace, Plane, Balloon, or Other.
> **Country**: The country location for the company's launchpad.
> **HQ Location**: The main office location fot the company.

## Goal
Find the **country** with the best average price to launch rockets into **low earth orbit (LEO)** for each launch class. Keep in mind the constraints laid out by the European Space Agency. Your analysis will allow the funding department to approach companies in the countries that offer the best value for each rocket class.

Save your answer as a single DataFrame and name it `launch_cost`. It should contain the country with the lowest average price (in $/Kg) for each rocket class.

Your resulting DataFrame should resemble the following, including identical column names:

Launch Class	| Average Price |	Country
Light |	xxxx |	xxxx
Medium |	xxxx |	xxxx
Heavy |	xxxx |	xxxx

