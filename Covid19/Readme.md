[API-docs](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#9739c95f-ef1d-489b-97a9-0a6dfe2f74d8)

# Backend:

### Return covid_backend.py `[global]`:
```
TotalConfirmed: 5.399.508
TotalDeaths: 362.859
TotalRecovered: 1.374.979

GlobalLethalityRate : 6.72%
*not accurate, because there are not tested infectious cases*
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

TotalConfirmed: 171.324
TotalDeaths: 7.549
TotalRecovered: 143.300

Deaths from Global: 2.08%
Cases from Global: 3.17%
Recovered from Global: 10.42%
Lethality rate in Germany: 4.41%
*not accurate, because there are not tested infectious cases*
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
