MONTHS_DICT = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
               'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

WORLDOMETER_NAME = {'brunei': 'brunei-darussalam',
                    'hong kong': 'china-hong-kong-sar',
                    'macao': 'china-macao-sar',
                    'congo': 'democratic-republic-of-the-congo',
                    'falkland islands': 'falkland-islands-malvinas',
                    'palestine': 'state-of-palestine',
                    'vietnam' : 'viet-nam',
                    }

COUNTRY_CODE_TO_NAME = {"AD": "andorra",
                        "AE": "united arab emirates",
                        "AF": "afghanistan",
                        "AG": "antigua and barbuda",
                        "AI": "anguilla",
                        "AL": "albania",
                        "AM": "armenia",
                        "AO": "angola",
                        "AQ": "antarctica",
                        "AR": "argentina",
                        "AS": "american samoa",
                        "AT": "austria",
                        "AU": "australia",
                        "AW": "aruba",
                        "AX": "aland islands",
                        "AZ": "azerbaijan",
                        "BA": "bosnia and herzegovina",
                        "BB": "barbados",
                        "BD": "bangladesh",
                        "BE": "belgium",
                        "BF": "burkina faso",
                        "BG": "bulgaria",
                        "BH": "bahrain",
                        "BI": "burundi",
                        "BJ": "benin",
                        "BL": "saint barthélemy",
                        "BM": "bermuda",
                        "BN": "brunei",
                        "BO": "bolivia",
                        "BQ": "bonaire",
                        "BR": "brazil",
                        "BS": "bahamas",
                        "BT": "bhutan",
                        "BV": "bouvet island",
                        "BW": "botswana",
                        "BY": "belarus",
                        "BZ": "belize",
                        "CA": "canada",
                        "CC": "cocos (keeling) islands",
                        "CD": "congo",
                        "CF": "central african republic",
                        "CG": "congo",
                        "CH": "switzerland",
                        "CI": "côte d'ivoire",
                        "CK": "cook islands",
                        "CL": "chile",
                        "CM": "cameroon",
                        "CN": "china",
                        "CO": "colombia",
                        "CR": "costa rica",
                        "CU": "cuba",
                        "CV": "cabo verde",
                        "CW": "curaçao",
                        "CX": "christmas island",
                        "CY": "cyprus",
                        "CZ": "czechia",
                        "DE": "germany",
                        "DJ": "djibouti",
                        "DK": "denmark",
                        "DM": "dominica",
                        "DO": "dominican republic",
                        "DZ": "algeria",
                        "EC": "ecuador",
                        "EE": "estonia",
                        "EG": "egypt",
                        "EH": "western sahara",
                        "ER": "eritrea",
                        "ES": "spain",
                        "ET": "ethiopia",
                        "FI": "finland",
                        "FJ": "fiji",
                        "FK": "falkland islands",
                        "FM": "micronesia (federated states of)",
                        "FO": "faroe islands",
                        "FR": "france",
                        "GA": "gabon",
                        "GB": "uk",
                        "GD": "grenada",
                        "GE": "georgia",
                        "GF": "french guiana",
                        "GG": "guernsey",
                        "GH": "ghana",
                        "GI": "gibraltar",
                        "GL": "greenland",
                        "GM": "gambia",
                        "GN": "guinea",
                        "GP": "guadeloupe",
                        "GQ": "equatorial guinea",
                        "GR": "greece",
                        "GS": "south georgia and the south sandwich islands",
                        "GT": "guatemala",
                        "GU": "guam",
                        "GW": "guinea-bissau",
                        "GY": "guyana",
                        "HK": "hong kong",
                        "HM": "heard island and mcdonald islands",
                        "HN": "honduras",
                        "HR": "croatia",
                        "HT": "haiti",
                        "HU": "hungary",
                        "ID": "indonesia",
                        "IE": "ireland",
                        "IL": "israel",
                        "IM": "isle of man",
                        "IN": "india",
                        "IO": "british indian ocean territory",
                        "IQ": "iraq",
                        "IR": "iran",
                        "IS": "iceland",
                        "IT": "italy",
                        "JE": "jersey",
                        "JM": "jamaica",
                        "JO": "jordan",
                        "JP": "japan",
                        "KE": "kenya",
                        "KG": "kyrgyzstan",
                        "KH": "cambodia",
                        "KI": "kiribati",
                        "KM": "comoros",
                        "KN": "saint kitts and nevis",
                        "KP": "north-korea",
                        "KR": "south-korea",
                        "KW": "kuwait",
                        "KY": "cayman islands",
                        "KZ": "kazakhstan",
                        "LA": "lao people's democratic republic",
                        "LB": "lebanon",
                        "LC": "saint lucia",
                        "LI": "liechtenstein",
                        "LK": "sri lanka",
                        "LR": "liberia",
                        "LS": "lesotho",
                        "LT": "lithuania",
                        "LU": "luxembourg",
                        "LV": "latvia",
                        "LY": "libya",
                        "MA": "morocco",
                        "MC": "monaco",
                        "MD": "moldova",
                        "ME": "montenegro",
                        "MF": "saint martin (french part)",
                        "MG": "madagascar",
                        "MH": "marshall islands",
                        "MK": "north macedonia",
                        "ML": "mali",
                        "MM": "myanmar",
                        "MN": "mongolia",
                        "MO": "macao",
                        "MP": "northern mariana islands",
                        "MQ": "martinique",
                        "MR": "mauritania",
                        "MS": "montserrat",
                        "MT": "malta",
                        "MU": "mauritius",
                        "MV": "maldives",
                        "MW": "malawi",
                        "MX": "mexico",
                        "MY": "malaysia",
                        "MZ": "mozambique",
                        "NA": "namibia",
                        "NC": "new caledonia",
                        "NE": "niger",
                        "NF": "norfolk island",
                        "NG": "nigeria",
                        "NI": "nicaragua",
                        "NL": "netherlands",
                        "NO": "norway",
                        "NP": "nepal",
                        "NR": "nauru",
                        "NU": "niue",
                        "NZ": "new zealand",
                        "OM": "oman",
                        "PA": "panama",
                        "PE": "peru",
                        "PF": "french polynesia",
                        "PG": "papua new guinea",
                        "PH": "philippines",
                        "PK": "pakistan",
                        "PL": "poland",
                        "PM": "saint pierre and miquelon",
                        "PN": "pitcairn",
                        "PR": "puerto rico",
                        "PS": "palestine, state of",
                        "PT": "portugal",
                        "PW": "palau",
                        "PY": "paraguay",
                        "QA": "qatar",
                        "RE": "réunion",
                        "RO": "romania",
                        "RS": "serbia",
                        "RU": "russia",
                        "RW": "rwanda",
                        "SA": "saudi arabia",
                        "SB": "solomon islands",
                        "SC": "seychelles",
                        "SD": "sudan",
                        "SE": "sweden",
                        "SG": "singapore",
                        "SH": "saint helena",
                        "SI": "slovenia",
                        "SJ": "svalbard and jan mayen",
                        "SK": "slovakia",
                        "SL": "sierra leone",
                        "SM": "san marino",
                        "SN": "senegal",
                        "SO": "somalia",
                        "SR": "suriname",
                        "SS": "south sudan",
                        "ST": "sao tome and principe",
                        "SV": "el salvador",
                        "SX": "sint maarten (dutch part)",
                        "SY": "syrian arab republic",
                        "SZ": "eswatini",
                        "TC": "turks and caicos islands",
                        "TD": "chad",
                        "TF": "french southern territories",
                        "TG": "togo",
                        "TH": "thailand",
                        "TJ": "tajikistan",
                        "TK": "tokelau",
                        "TL": "timor-leste",
                        "TM": "turkmenistan",
                        "TN": "tunisia",
                        "TO": "tonga",
                        "TR": "turkey",
                        "TT": "trinidad and tobago",
                        "TV": "tuvalu",
                        "TW": "taiwan",
                        "TZ": "tanzania",
                        "UA": "ukraine",
                        "UG": "uganda",
                        "UM": "united states minor outlying islands",
                        "US": "us",
                        "UY": "uruguay",
                        "UZ": "uzbekistan",
                        "VA": "holy see",
                        "VC": "saint vincent and the grenadines",
                        "VE": "venezuela",
                        "VG": "virgin islands (british)",
                        "VI": "virgin islands (u.s.)",
                        "VN": "vietnam",
                        "VU": "vanuatu",
                        "WF": "wallis and futuna",
                        "WS": "samoa",
                        "YE": "yemen",
                        "YT": "mayotte",
                        "ZA": "south africa",
                        "ZM": "zambia",
                        "ZW": "zimbabwe",
                        }

COUNTRY_NAME_TO_CODE = {v: k for k, v in COUNTRY_CODE_TO_NAME.items()}

# Population copied from https://www.worldometers.info/world-population/population-by-country/ on 26-Mar-2020
POPULATIONS = {
    'world': 7713468100,
    'afghanistan': 38928346,
    'albania': 2877797,
    'algeria': 43851044,
    'american samoa': 55191,
    'andorra': 77265,
    'angola': 32866272,
    'anguilla': 15003,
    'antigua and barbuda': 97929,
    'argentina': 45195774,
    'armenia': 2963243,
    'aruba': 106766,
    'australia': 25499884,
    'austria': 9006398,
    'azerbaijan': 10139177,
    'bahamas': 393244,
    'bahrain': 1701575,
    'bangladesh': 164689383,
    'barbados': 287375,
    'belarus': 9449323,
    'belgium': 11589623,
    'belize': 397628,
    'benin': 12123200,
    'bermuda': 62278,
    'bhutan': 771608,
    'bolivia': 11673021,
    'bosnia and herzegovina': 3280819,
    'botswana': 2351627,
    'brazil': 212559417,
    'british virgin islands': 30231,
    'brunei': 437479,
    'bulgaria': 6948445,
    'burkina faso': 20903273,
    'burundi': 11890784,
    'cabo verde': 555987,
    'cambodia': 16718965,
    'cameroon': 26545863,
    'canada': 37742154,
    'caribbean netherlands': 26223,
    'cayman islands': 65722,
    'central african republic': 4829767,
    'chad': 16425864,
    'channel islands': 173863,
    'chile': 19116201,
    'china': 1439323776,
    'colombia': 50882891,
    'comoros': 869601,
    'congo': 5518087,
    'cook islands': 17564,
    'costa rica': 5094118,
    'croatia': 4105267,
    'cuba': 11326616,
    'curaçao': 164093,
    'cyprus': 1207359,
    'czechia': 10708981,
    'denmark': 5792202,
    'djibouti': 988000,
    'dominica': 71986,
    'dominican republic': 10847910,
    'dr congo': 89561403,
    'ecuador': 17643054,
    'egypt': 102334404,
    'el salvador': 6486205,
    'equatorial guinea': 1402985,
    'eritrea': 3546421,
    'estonia': 1326535,
    'eswatini': 1160164,
    'ethiopia': 114963588,
    'faeroe islands': 48863,
    'falkland islands': 3480,
    'fiji': 896445,
    'finland': 5540720,
    'france': 65273511,
    'french guiana': 298682,
    'french polynesia': 280908,
    'gabon': 2225734,
    'gambia': 2416668,
    'georgia': 3989167,
    'germany': 83783942,
    'ghana': 31072940,
    'gibraltar': 33691,
    'greece': 10423054,
    'greenland': 56770,
    'grenada': 112523,
    'guadeloupe': 400124,
    'guam': 168775,
    'guatemala': 17915568,
    'guinea': 13132795,
    'guinea-bissau': 1968001,
    'guyana': 786552,
    'haiti': 11402528,
    'holy see': 801,
    'honduras': 9904607,
    'hong kong': 7496981,
    'hungary': 9660351,
    'iceland': 341243,
    'india': 1380004385,
    'indonesia': 273523615,
    'iran': 83992949,
    'iraq': 40222493,
    'ireland': 4937786,
    'isle of man': 85033,
    'israel': 8655535,
    'italy': 60461826,
    'jamaica': 2961167,
    'japan': 126476461,
    'jordan': 10203134,
    'kazakhstan': 18776707,
    'kenya': 53771296,
    'kiribati': 119449,
    'kuwait': 4270571,
    'kyrgyzstan': 6524195,
    'laos': 7275560,
    'latvia': 1886198,
    'lebanon': 6825445,
    'lesotho': 2142249,
    'liberia': 5057681,
    'libya': 6871292,
    'liechtenstein': 38128,
    'lithuania': 2722289,
    'luxembourg': 625978,
    'macao': 649335,
    'madagascar': 27691018,
    'malawi': 19129952,
    'malaysia': 32365999,
    'maldives': 540544,
    'mali': 20250833,
    'malta': 441543,
    'marshall islands': 59190,
    'martinique': 375265,
    'mauritania': 4649658,
    'mauritius': 1271768,
    'mayotte': 272815,
    'mexico': 128932753,
    'micronesia': 115023,
    'moldova': 4033963,
    'monaco': 39242,
    'mongolia': 3278290,
    'montenegro': 628066,
    'montserrat': 4992,
    'morocco': 36910560,
    'mozambique': 31255435,
    'myanmar': 54409800,
    'namibia': 2540905,
    'nauru': 10824,
    'nepal': 29136808,
    'netherlands': 17134872,
    'new caledonia': 285498,
    'new zealand': 4822233,
    'nicaragua': 6624554,
    'niger': 24206644,
    'nigeria': 206139589,
    'niue': 1626,
    'north korea': 25778816,
    'north macedonia': 2083374,
    'northern mariana islands': 57559,
    'norway': 5421241,
    'oman': 5106626,
    'pakistan': 220892340,
    'palau': 18094,
    'panama': 4314767,
    'papua new guinea': 8947024,
    'paraguay': 7132538,
    'peru': 32971854,
    'philippines': 109581078,
    'poland': 37846611,
    'portugal': 10196709,
    'puerto rico': 2860853,
    'qatar': 2881053,
    'romania': 19237691,
    'russia': 145934462,
    'rwanda': 12952218,
    'réunion': 895312,
    'saint barthelemy': 9877,
    'saint helena': 6077,
    'saint kitts & nevis': 53199,
    'saint lucia': 183627,
    'saint martin': 38666,
    'saint pierre & miquelon': 5794,
    'samoa': 198414,
    'san marino': 33931,
    'sao tome & principe': 219159,
    'saudi arabia': 34813871,
    'senegal': 16743927,
    'serbia': 8737371,
    'seychelles': 98347,
    'sierra leone': 7976983,
    'singapore': 5850342,
    'sint maarten': 42876,
    'slovakia': 5459642,
    'slovenia': 2078938,
    'solomon islands': 686884,
    'somalia': 15893222,
    'south africa': 59308690,
    'south-korea': 51269185,
    'south sudan': 11193725,
    'spain': 46754778,
    'sri lanka': 21413249,
    'st. vincent & grenadines': 110940,
    'state of palestine': 5101414,
    'sudan': 43849260,
    'suriname': 586632,
    'sweden': 10099265,
    'switzerland': 8654622,
    'syria': 17500658,
    'taiwan': 23816775,
    'tajikistan': 9537645,
    'tanzania': 59734218,
    'thailand': 69799978,
    'timor-leste': 1318445,
    'togo': 8278724,
    'tokelau': 1357,
    'tonga': 105695,
    'trinidad and tobago': 1399488,
    'tunisia': 11818619,
    'turkey': 84339067,
    'turkmenistan': 6031200,
    'turks and caicos': 38717,
    'tuvalu': 11792,
    'u.s. virgin islands': 104425,
    'uganda': 45741007,
    'ukraine': 43733762,
    'united arab emirates': 9890402,
    'uk': 67886011,
    'us': 331002651,
    'uruguay': 3473730,
    'uzbekistan': 33469203,
    'vanuatu': 307145,
    'venezuela': 28435940,
    'vietnam': 97338579,
    'wallis & futuna': 11239,
    'western sahara': 597339,
    'yemen': 29825964,
    'zambia': 18383955,
    'zimbabwe': 14862924,
}