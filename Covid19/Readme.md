[API-docs](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#9739c95f-ef1d-489b-97a9-0a6dfe2f74d8)

# Backend:

### Return covid_backend.py `[global]`:

```
NewConfirmed: 81849
TotalConfirmed: 2519183
NewDeaths: 6788
TotalDeaths: 172976
NewRecovered: 34329
TotalRecovered: 679101
2020-04-22T14:28:43Z
```
### Return covid_backend.py `[displayAllCountries]`:

[ReturnObject](https://raw.githubusercontent.com/xNaCly/scripts/master/Covid19/available_countries.txt)

### Return covid_backend.py `[oneCountry] [country] | [oneCountry] [DE]`:
#### country: [DE, Germany] <br>- not casesensitive <br>- accepts: CountryCode or Country(Name) or country Slug
```
Country: DE
Country: Germany
CountryCode: DE
Slug: germany
NewConfirmed: 0
TotalConfirmed: 167007
NewDeaths: 0
TotalDeaths: 6993
NewRecovered: 0
TotalRecovered: 135100
Date: 2020-05-06T20:24:50Z

Deaths relative to Global: 2.72%
Cases relative to Total: 4.56%
```

### Return covid_backend.py `[displayLeaderboards] [type] | [displayLeaderboards] [deaths]`:
#### type: [cases, deaths, recovered] <br>-not casesensitive <br>- accepts 3 types
```
United States of America: 157.537
United Kingdom: 31.662
Italy: 30.395
Spain: 26.478
France: 26.313
```
