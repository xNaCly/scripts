import covid_backend

# returns global covid19 data
print(covid_backend.globalStats())

"""
TotalConfirmed: 5.399.508
TotalDeaths: 362.859
TotalRecovered: 1.374.979

GlobalLethalityRate : 6.72%
*not accurate, because there are not tested infectious cases*
"""

# returns covid19 data for the US
print(covid_backend.displayOneCountry("US"))

"""
Country: United States of America
CountryCode: US
Slug: united-states

TotalConfirmed: 2.616.854
TotalDeaths: 157.537
TotalRecovered: 212.534

Deaths from Global: 43.42%
Cases from Global: 48.46%
Recovered from Global: 15.46%
Lethality rate in United States of America: 6.02%
*not accurate, because there are not tested infectious cases*
"""

# returns covid19 leaderboards for deaths (top5)
print(covid_backend.displayLeaderboards("deaths"))

"""
United States of America: 157.537
United Kingdom: 31.662
Italy: 30.395
Spain: 26.478
France: 26.313
"""

# returns all available countries
print(covid_backend.displayAllCountries())

"""
Afghanistan | AF
Albania | AL
Algeria | DZ
Andorra | AD
Angola | AO
Antigua and Barbuda | AG
Argentina | AR
Armenia | AM
Australia | AU
Austria | AT
Azerbaijan | AZ
Bahamas | BS
Bahrain | BH
Bangladesh | BD
Barbados | BB
Belarus | BY
Belgium | BE
Belize | BZ
Benin | BJ
Bhutan | BT
Bolivia | BO
Bosnia and Herzegovina | BA
Botswana | BW
Brazil | BR
Brunei Darussalam | BN
Bulgaria | BG
Burkina Faso | BF
Burundi | BI
Cambodia | KH
Cameroon | CM
Canada | CA
Cape Verde | CV
Central African Republic | CF
Chad | TD
Chile | CL
China | CN
Colombia | CO
Comoros | KM
Congo (Brazzaville) | CG
Congo (Kinshasa) | CD
Costa Rica | CR
Croatia | HR
Cuba | CU
Cyprus | CY
Czech Republic | CZ
Côte d'Ivoire | CI
Denmark | DK
Djibouti | DJ
Dominica | DM
Dominican Republic | DO
Ecuador | EC
Egypt | EG
El Salvador | SV
Equatorial Guinea | GQ
Eritrea | ER
Estonia | EE
Ethiopia | ET
Fiji | FJ
Finland | FI
France | FR
Gabon | GA
Gambia | GM
Georgia | GE
Germany | DE
Ghana | GH
Greece | GR
Grenada | GD
Guatemala | GT
Guinea | GN
Guinea-Bissau | GW
Guyana | GY
Haiti | HT
Holy See (Vatican City State) | VA
Honduras | HN
Hungary | HU
Iceland | IS
India | IN
Indonesia | ID
Iran, Islamic Republic of | IR
Iraq | IQ
Ireland | IE
Israel | IL
Italy | IT
Jamaica | JM
Japan | JP
Jordan | JO
Kazakhstan | KZ
Kenya | KE
Korea (South) | KR
Kuwait | KW
Kyrgyzstan | KG
Lao PDR | LA
Latvia | LV
Lebanon | LB
Liberia | LR
Libya | LY
Liechtenstein | LI
Lithuania | LT
Luxembourg | LU
Macedonia, Republic of | MK
Madagascar | MG
Malawi | MW
Malaysia | MY
Maldives | MV
Mali | ML
Malta | MT
Mauritania | MR
Mauritius | MU
Mexico | MX
Moldova | MD
Monaco | MC
Mongolia | MN
Montenegro | ME
Morocco | MA
Mozambique | MZ
Myanmar | MM
Namibia | NA
Nepal | NP
Netherlands | NL
New Zealand | NZ
Nicaragua | NI
Niger | NE
Nigeria | NG
Norway | NO
Oman | OM
Pakistan | PK
Palestinian Territory | PS
Panama | PA
Papua New Guinea | PG
Paraguay | PY
Peru | PE
Philippines | PH
Poland | PL
Portugal | PT
Qatar | QA
Republic of Kosovo | XK
Romania | RO
Russian Federation | RU
Rwanda | RW
Saint Kitts and Nevis | KN
Saint Lucia | LC
Saint Vincent and Grenadines | VC
San Marino | SM
Sao Tome and Principe | ST
Saudi Arabia | SA
Senegal | SN
Serbia | RS
Seychelles | SC
Sierra Leone | SL
Singapore | SG
Slovakia | SK
Slovenia | SI
Somalia | SO
South Africa | ZA
South Sudan | SS
Spain | ES
Sri Lanka | LK
Sudan | SD
Suriname | SR
Swaziland | SZ
Sweden | SE
Switzerland | CH
Syrian Arab Republic (Syria) | SY
Taiwan, Republic of China | TW
Tajikistan | TJ
Tanzania, United Republic of | TZ
Thailand | TH
Timor-Leste | TL
Togo | TG
Trinidad and Tobago | TT
Tunisia | TN
Turkey | TR
Uganda | UG
Ukraine | UA
United Arab Emirates | AE
United Kingdom | GB
United States of America | US
Uruguay | UY
Uzbekistan | UZ
Venezuela (Bolivarian Republic) | VE
Viet Nam | VN
Western Sahara | EH
Yemen | YE
Zambia | ZM
Zimbabwe | ZW
"""
