

# Backend [covid_backend.py](https://github.com/xNaCly/scripts/blob/master/Covid19/covid_backend.py):
[API-docs](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#9739c95f-ef1d-489b-97a9-0a6dfe2f74d8)
- wrapper for ^ 
- makes usability in other projects easier

## Important methods:

### `[global]`:
```
TotalConfirmed: 5.399.508
TotalDeaths: 362.859
TotalRecovered: 1.374.979

GlobalLethalityRate : 6.72%
*not accurate, because there are not tested infectious cases*
```
### `[displayAllCountries]`:

[ReturnObject](https://raw.githubusercontent.com/xNaCly/scripts/master/Covid19/available_countries.txt)

### covid_backend.py `[oneCountry] [country]`:
#### country: [DE, Germany] 
- not casesensitive 
- accepts: CountryCode or Country(Name) or country Slug
```
[oneCountry] [DE]:

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

### `[displayLeaderboards] [type]`:
#### type: [cases, deaths, recovered] 
-not casesensitive 
- accepts 3 types
```
[displayLeaderboards] [deaths]

United States of America: 157.537
United Kingdom: 31.662
Italy: 30.395
Spain: 26.478
France: 26.313
```

## Less important methods:

### `[errorLogger] [error]`:
- as the name suggests, logs error to `log`-file

### covid_backend.py `[makeReadable] [number]`:
- converts number to easier readable number
- if input isnt a number --> returns same var as the input
```
1000    --> 1.000
10000   --> 10.000
100000  --> 100.000
1000000 --> 1.000.000
```

### `[theRequest]`:
- makes request to the [api](https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#9739c95f-ef1d-489b-97a9-0a6dfe2f74d8)
- if cant access the api, due to whatever --> throws an [error](https://github.com/xNaCly/scripts/tree/master/Covid19#covid_backendpy-errorlogger-error)

### `[requestStats]`:
- everytime a method is called this function runs a new request to the api
- calls [theRequest](https://github.com/xNaCly/scripts/tree/master/Covid19#covid_backendpy-therequest)
