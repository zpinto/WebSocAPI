# WebSoc API

---

# Introduction

Returns data on UCI classes by scrapping WebSoc. Classes can be filtered by departments and breadths, as well as other query paramteters.

# Overview

This service is in its early stages and will likely see significant updates, deprecating functionalities currently avaliable.

# Authentication

There is no authentication in this iteration of the service.

# Error Codes

200 - data was returned ok
404 - data not found
500 - internal server error

# Rate limit

There is no limit on the number of requests. A future iteration of this API will have authentication and all users will have to register and be approved. Upon approval, your account will be created.

---

## /filters

```
GET {{url}}/filters
```

Returns all of the possible filters/query params that can be used to select classes.

---

### Request

>

### Examples:

> **Example: /filters**
>
> > ```
> > GET {{url}}/filters
> > ```
> >
> > **Request**
> >
> > >
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   "YearTerm": "Year and Term",
> > >   "Breadth": "Breadth Ex. AFAM, ANATOMY, ART",
> > >   "Dept": "Department Ex. AFAM, ANATOMY, ART",
> > >   "CourseNum": "Course Number Ex. 53, 53L",
> > >   "Division": "Division Ex. ANY, 0xx, 1xx, 2xx",
> > >   "CourseCodes": "Course Codes Ex. 14200, 29000-29010"
> > > }
> > > ```

---

## /Breadths

```
GET {{url}}/Breadths
```

Returns a list of the possible breadths maped to their codes.

---

### Request

>

### Examples:

> **Example: /Breadths**
>
> > ```
> > GET {{url}}/Breadths
> > ```
> >
> > **Request**
> >
> > >
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   "2": "Breadth II: Natural Sciences",
> > >   "3": "Breadth III: Social and Behavioral Sciences",
> > >   "4": "Breadth IV: Humanistic Inquiry",
> > >   "5": "Breadth V: Mathematics and Symbolic Systems",
> > >   "6": "Breadth VI: Language Other Than English",
> > >   "ANY": "\u00a0\u00a0\u00a0\u00a0--- Breadth categories (prior to Fall 2008) ---",
> > >   "GE-1A": "GE Ia: Lower Division Writing",
> > >   "GE-1B": "GE Ib: Upper Division Writing",
> > >   "GE-2": "GE II: Science and Technology",
> > >   "GE-3": "GE III: Social and Behavioral Sciences",
> > >   "GE-4": "GE IV: Arts and Humanities",
> > >   "GE-5A": "GE Va: Quantitative Literacy (starting Fall 2012)",
> > >   "GE-5B": "GE Vb: Formal Reasoning (starting Fall 2012)",
> > >   "GE-6": "GE VI: Language other than English",
> > >   "GE-7": "GE VII: Multicultural Studies",
> > >   "GE-8": "GE VIII: International/Global Issues",
> > >   "GE-5": "GE V: Quantitative, Symbolic, and Computational Reasoning",
> > >   "GE-9": "GE IX: Laboratory or Performance",
> > >   "1A": "Breadth Ia: Lower Division Writing",
> > >   "1B": "Breadth Ib: Upper Division Writing",
> > >   "7A": "Breadth VIIa: Multicultural Studies",
> > >   "7B": "Breadth VIIb: International/global Issues"
> > > }
> > > ```

---

## /Breadth/<breadth_name>

```
GET {{url}}/Breadth/4
```

Returns all of the classes under a specified Breadth.

---

### Request

>

### Examples:

>

---

## /Depts

```
GET {{url}}/Depts
```

Returns a list of all of the possible departments mapped to their code.

---

### Request

>

### Examples:

> **Example: /Depts**
>
> > ```
> > GET {{url}}/Depts
> > ```
> >
> > **Request**
> >
> > >
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   " ALL": "Include All Departments",
> > >   "AC ENG": "AC ENG . . . . . .Academic English and ESL",
> > >   "AFAM": "AFAM . . . . . . . African American Studies",
> > >   "ANATOMY": "ANATOMY . . . .Anatomy and Neurobiology",
> > >   "ANESTH": "ANESTH . . . . . Anesthesiology",
> > >   "ANTHRO": "ANTHRO . . . . . Anthropology",
> > >   "ARABIC": "ARABIC . . . . . .Arabic",
> > >   "ARMN": "ARMN . . . . . . .Armenian (started 2018 Spg)",
> > >   "ART": "ART . . . . . . . . .Art",
> > >   "ART HIS": "ART HIS . . . . . .Art History",
> > >   "ARTS": "ARTS . . . . . . . Arts",
> > >   "ARTSHUM": "ARTSHUM . . . . Arts and Humanities",
> > >   "ASIANAM": "ASIANAM . . . . Asian American Studies",
> > >   "BANA": "BANA . . . . . . . Business Analytics (started 2017 SS2)",
> > >   "BATS": "BATS . . . . . . . Biomedical and Translational Science",
> > >   "BIO SCI": "BIO SCI . . . . . .Biological Sciences",
> > >   "BIOCHEM": "BIOCHEM . . . . Biological Chemistry",
> > >   "BME": "BME . . . . . . . . Biomedical Engineering",
> > >   "BSEMD": "BSEMD . . . . . .Bio Sci & Educational Media Design (until 2017 Wtr)",
> > >   "CAMPREC": "CAMPREC . . . .Campus Recreation",
> > >   "CBE": "CBE . . . . . . . . Chemical and Biomolecular Engineering (started 2018 Fall)",
> > >   "CBEMS": "CBEMS . . . . . .Chemical Engr and Materials Science",
> > >   "CEM": "CEM . . . . . . . . Community and Environmental Medicine",
> > >   "CHC/LAT": "CHC/LAT . . . . . Chicano Latino",
> > >   "CHEM": "CHEM . . . . . . .Chemistry",
> > >   "CHINESE": "CHINESE . . . . .Chinese",
> > >   "CLASSIC": "CLASSIC . . . . .Classics",
> > >   "CLT&THY": "CLT&THY . . . . .Culture & Theory",
> > >   "COGS": "COGS . . . . . . . Cognitive Sciences  (started 2016 Fall)",
> > >   "COM LIT": "COM LIT . . . . . Comparative Literature",
> > >   "COMPSCI": "COMPSCI . . . . Computer Science",
> > >   "CRITISM": "CRITISM . . . . . Criticism",
> > >   "CRM/LAW": "CRM/LAW . . . . Criminology, Law and Society",
> > >   "CSE": "CSE . . . . . . . . Computer Science and Engineering",
> > >   "DANCE": "DANCE . . . . . . Dance",
> > >   "DERM": "DERM . . . . . . .Dermatology",
> > >   "DEV BIO": "DEV BIO . . . . . Developmental and Cell Biology",
> > >   "DRAMA": "DRAMA . . . . . .Drama",
> > >   "E ASIAN": "E ASIAN . . . . . East Asian Languages and Literatures (until 2019 SS2)",
> > >   "EARTHSS": "EARTHSS . . . . Earth System Science",
> > >   "EAS": "EAS . . . . . . . . East Asian Studies (started 2019 Fall)",
> > >   "ECO EVO": "ECO EVO . . . . Ecology and Evolutionary Biology",
> > >   "ECON": "ECON . . . . . . . Economics",
> > >   "ECPS": "ECPS . . . . . . . Embedded and Cyber-Physical Systems (started 2014 Spg)",
> > >   "ED AFF": "ED AFF . . . . . .Educational Affairs (Sch of Med)",
> > >   "EDUC": "EDUC . . . . . . . Education",
> > >   "EECS": "EECS . . . . . . . Electrical Engineering & Computer Science",
> > >   "EHS": "EHS . . . . . . . . Environmental Health Sciences",
> > >   "ENGLISH": "ENGLISH . . . . .English",
> > >   "ENGR": "ENGR . . . . . . . Engineering",
> > >   "ENGRCEE": "ENGRCEE . . . .Engineering, Civil and Environmental",
> > >   "ENGRMAE": "ENGRMAE . . . .Engineering, Mechanical and Aerospace",
> > >   "ENGRMSE": "ENGRMSE . . . .Materials Science and Engineering",
> > >   "EPIDEM": "EPIDEM . . . . . .Epidemiology",
> > >   "ER MED": "ER MED . . . . . Emergency Medicine",
> > >   "EURO ST": "EURO ST . . . . .European Studies",
> > >   "FAM MED": "FAM MED . . . . Family Medicine",
> > >   "FIN": "FIN . . . . . . . . . Finance (started 2017 Fall)",
> > >   "FLM&MDA": "FLM&MDA . . . .Film and Media Studies",
> > >   "FRENCH": "FRENCH . . . . . French",
> > >   "GEN&SEX": "GEN&SEX . . . . Gender and Sexuality Studies (started 2014 Fall)",
> > >   "GERMAN": "GERMAN . . . . .German",
> > >   "GLBL ME": "GLBL ME . . . . .Global Middle East Studies (started 2016 Fall)",
> > >   "GLBLCLT": "GLBLCLT . . . . .Global Cultures",
> > >   "GREEK": "GREEK . . . . . . Greek",
> > >   "HEBREW": "HEBREW . . . . .Hebrew",
> > >   "HINDI": "HINDI . . . . . . . .Hindi",
> > >   "HISTORY": "HISTORY . . . . .History",
> > >   "HUMAN": "HUMAN . . . . . .Humanities",
> > >   "HUMARTS": "HUMARTS . . . . Humanities and Arts",
> > >   "I&C SCI": "I&C SCI . . . . . . Information and Computer Science",
> > >   "IN4MATX": "IN4MATX . . . . . Informatics",
> > >   "INNO": "INNO . . . . . . . .Masters of Innovation and Entrepreneurship (started 2019 Fall)",
> > >   "INT MED": "INT MED . . . . . Internal Medicine",
> > >   "INTL ST": "INTL ST . . . . . . International Studies",
> > >   "ITALIAN": "ITALIAN . . . . . .Italian",
> > >   "JAPANSE": "JAPANSE . . . . Japanese",
> > >   "KOREAN": "KOREAN . . . . .Korean",
> > >   "LATIN": "LATIN . . . . . . . Latin",
> > >   "LAW": "LAW . . . . . . . . Law",
> > >   "LINGUIS": "LINGUIS . . . . . .Linguistics (until 2019 SS2)",
> > >   "LIT JRN": "LIT JRN . . . . . . Literary Journalism",
> > >   "LPS": "LPS . . . . . . . . .Logic and Philosophy of Science",
> > >   "LSCI": "LSCI . . . . . . . . Language Science (started 2019 Fall)",
> > >   "M&MG": "M&MG . . . . . . .Microbiology and Molecular Genetics",
> > >   "MATH": "MATH . . . . . . . Mathematics",
> > >   "MED": "MED . . . . . . . . Medicine",
> > >   "MED ED": "MED ED . . . . . Medical Education",
> > >   "MED HUM": "MED HUM . . . . Medical Humanities (started 2016 Fall)",
> > >   "MGMT": "MGMT . . . . . . .Management",
> > >   "MGMT EP": "MGMT EP . . . . Executive MBA",
> > >   "MGMT FE": "MGMT FE . . . . Fully Employed MBA",
> > >   "MGMT HC": "MGMT HC . . . . Health Care MBA",
> > >   "MGMTMBA": "MGMTMBA . . . Management MBA",
> > >   "MGMTPHD": "MGMTPHD . . . .Management PhD",
> > >   "MIC BIO": "MIC BIO . . . . . .Microbiology",
> > >   "MOL BIO": "MOL BIO . . . . . Molecular Biology and Biochemistry",
> > >   "MPAC": "MPAC . . . . . . .Accounting",
> > >   "MSE": "MSE . . . . . . . . Materials Science and Engineering (2018 Fall to 2018 Fall)",
> > >   "MUSIC": "MUSIC . . . . . . .Music",
> > >   "NET SYS": "NET SYS . . . . .Networked Systems",
> > >   "NEURBIO": "NEURBIO . . . . .Neurobiology and Behavior",
> > >   "NEUROL": "NEUROL . . . . . Neurology",
> > >   "NUR SCI": "NUR SCI . . . . . Nursing Science",
> > >   "OB/GYN": "OB/GYN . . . . . Obstetrics and Gynecology",
> > >   "OPHTHAL": "OPHTHAL . . . . Ophthalmology",
> > >   "PATH": "PATH . . . . . . . Pathology and Laboratory Medicine",
> > >   "PED GEN": "PED GEN . . . . Pediatrics Genetics",
> > >   "PEDS": "PEDS . . . . . . . Pediatrics",
> > >   "PERSIAN": "PERSIAN . . . . .Persian",
> > >   "PHARM": "PHARM . . . . . .Medical Pharmacology",
> > >   "PHILOS": "PHILOS . . . . . .Philosophy",
> > >   "PHRMSCI": "PHRMSCI . . . . Pharmaceutical Sciences",
> > >   "PHY SCI": "PHY SCI . . . . . Physical Science",
> > >   "PHYSICS": "PHYSICS . . . . .Physics",
> > >   "PHYSIO": "PHYSIO . . . . . .Physiology and Biophysics",
> > >   "PLASTIC": "PLASTIC . . . . . Plastic Surgery (started 2014 Fall)",
> > >   "PM&R": "PM&R . . . . . . .Physical Medicine and Rehabilitation",
> > >   "POL SCI": "POL SCI . . . . . Political Science",
> > >   "PORTUG": "PORTUG . . . . . Portuguese",
> > >   "PP&D": "PP&D . . . . . . . Planning, Policy, and Design (until 2018 SS2; see UPPP)",
> > >   "PSCI": "PSCI . . . . . . . .Psychological Science (started 2019 Fall)",
> > >   "PSY BEH": "PSY BEH . . . . .Psychology and Social Behavior (until 2019 SS2)",
> > >   "PSYCH": "PSYCH . . . . . . Psychology",
> > >   "PUB POL": "PUB POL . . . . .Public Policy",
> > >   "PUBHLTH": "PUBHLTH . . . . Public Health",
> > >   "RADIO": "RADIO . . . . . . .Radiology",
> > >   "REL STD": "REL STD . . . . . Religious Studies",
> > >   "ROTC": "ROTC . . . . . . . Reserve Officers' Training Corps",
> > >   "RUSSIAN": "RUSSIAN . . . . .Russian",
> > >   "SOC SCI": "SOC SCI . . . . . Social Science",
> > >   "SOCECOL": "SOCECOL . . . . Social Ecology",
> > >   "SOCIOL": "SOCIOL . . . . . .Sociology",
> > >   "SPANISH": "SPANISH . . . . .Spanish",
> > >   "SPPS": "SPPS . . . . . . . Social Policy & Public Service (started 2016 Wtr)",
> > >   "STATS": "STATS . . . . . . .Statistics",
> > >   "SURGERY": "SURGERY . . . .Surgery",
> > >   "SWE": "SWE . . . . . . . .Software Engineering (started 2019 Fall)",
> > >   "TAGALOG": "TAGALOG . . . . Tagalog",
> > >   "TOX": "TOX . . . . . . . . .Toxicology",
> > >   "UCDC": "UCDC . . . . . . . UC Washington DC",
> > >   "UNI AFF": "UNI AFF . . . . . .University Affairs",
> > >   "UNI STU": "UNI STU . . . . . .University Studies",
> > >   "UPPP": "UPPP . . . . . . . Urban Planning and Public Policy (started 2018 Fall)",
> > >   "VIETMSE": "VIETMSE . . . . .Vietnamese",
> > >   "VIS STD": "VIS STD . . . . . .Visual Studies",
> > >   "WOMN ST": "WOMN ST . . . . Women's Studies (until 2014 SS2)",
> > >   "WRITING": "WRITING . . . . . Writing"
> > > }
> > > ```

---

## /Dept/<department_name>

```
GET {{url}}/Dept/VIETMSE
```

Returns all of the classes under a specified Department.

---

### Request

>

### Examples:

> **Example: /Dept/VIETMSE**
>
> > ```
> > GET {{url}}/Dept/VIETMSE
> > ```
> >
> > **Request**
> >
> > >
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   "32410": {
> > >     "code": "32410",
> > >     "type": "Lec",
> > >     "sec": "A",
> > >     "units": "5",
> > >     "instructor": "TRAN, T.",
> > >     "time": "MW  10:00-11:50 /F  10:00-10:50 ",
> > >     "place": "HICF 100Q///HICF 100Q",
> > >     "final": "Tue, Dec 10, 1:30-3:30pm",
> > >     "max": "24",
> > >     "enr": "11",
> > >     "wl": "0",
> > >     "req": "44",
> > >     "nor": "0",
> > >     "rstr": "A",
> > >     "status": "OPEN"
> > >   },
> > >   "32430": {
> > >     "code": "32430",
> > >     "type": "Lec",
> > >     "sec": "A",
> > >     "units": "4",
> > >     "instructor": "TRAN, T.",
> > >     "time": "TuTh  10:00-11:50 ",
> > >     "place": "HH 112",
> > >     "final": "Thu, Dec 12, 10:30-12:30pm",
> > >     "max": "24",
> > >     "enr": "5",
> > >     "wl": "0",
> > >     "req": "13",
> > >     "nor": "0",
> > >     "rstr": "A",
> > >     "status": "OPEN"
> > >   },
> > >   "32450": {
> > >     "code": "32450",
> > >     "type": "Act",
> > >     "sec": "A",
> > >     "units": "1",
> > >     "instructor": "STAFF",
> > >     "time": "  TBA",
> > >     "place": "TBA",
> > >     "final": "  TBA",
> > >     "max": "15",
> > >     "enr": "0",
> > >     "wl": "n/a",
> > >     "req": "1",
> > >     "nor": "0",
> > >     "rstr": "B and D",
> > >     "status": "OPEN"
> > >   },
> > >   "32460": {
> > >     "code": "32460",
> > >     "type": "Act",
> > >     "sec": "A",
> > >     "units": "1",
> > >     "instructor": "STAFF",
> > >     "time": "  TBA",
> > >     "place": "TBA",
> > >     "final": "  TBA",
> > >     "max": "15",
> > >     "enr": "0",
> > >     "wl": "n/a",
> > >     "req": "0",
> > >     "nor": "0",
> > >     "rstr": "B and D",
> > >     "status": "OPEN"
> > >   }
> > > }
> > > ```

---

## /YearTerms

```
GET {{url}}/YearTerms
```

Returns a list of the possible YearTerms mapped to their codes.

---

### Request

>

### Examples:

> **Example: /YearTerms**
>
> > ```
> > GET {{url}}/YearTerms
> > ```
> >
> > **Request**
> >
> > >
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   "2019-92": "2019  Fall Quarter",
> > >   "2019-76": "2019  Summer Session 2",
> > >   "2019-51": "2019  Summer Qtr (COM)",
> > >   "2019-39": "2019  10-wk Summer",
> > >   "2019-25": "2019  Summer Session 1",
> > >   "2019-14": "2019  Spring Quarter",
> > >   "2019-03": "2019  Winter Quarter",
> > >   "2018-92": "2018  Fall Quarter",
> > >   "2018-76": "2018  Summer Session 2",
> > >   "2018-51": "2018  Summer Qtr (COM)",
> > >   "2018-39": "2018  10-wk Summer",
> > >   "2018-25": "2018  Summer Session 1",
> > >   "2018-14": "2018  Spring Quarter",
> > >   "2018-03": "2018  Winter Quarter",
> > >   "2017-92": "2017  Fall Quarter",
> > >   "2017-76": "2017  Summer Session 2",
> > >   "2017-51": "2017  Summer Qtr (COM)",
> > >   "2017-39": "2017  10-wk Summer",
> > >   "2017-25": "2017  Summer Session 1",
> > >   "2017-14": "2017  Spring Quarter",
> > >   "2017-03": "2017  Winter Quarter",
> > >   "2016-92": "2016  Fall Quarter",
> > >   "2016-76": "2016  Summer Session 2",
> > >   "2016-51": "2016  Summer Qtr (COM)",
> > >   "2016-39": "2016  10-wk Summer",
> > >   "2016-25": "2016  Summer Session 1",
> > >   "2016-14": "2016  Spring Quarter",
> > >   "2016-03": "2016  Winter Quarter",
> > >   "2015-92": "2015  Fall Quarter",
> > >   "2015-76": "2015  Summer Session 2",
> > >   "2015-51": "2015  Summer Qtr (COM)",
> > >   "2015-39": "2015  10-wk Summer",
> > >   "2015-25": "2015  Summer Session 1",
> > >   "2015-14": "2015  Spring Quarter",
> > >   "2015-03": "2015  Winter Quarter",
> > >   "2014-92": "2014  Fall Quarter",
> > >   "2014-76": "2014  Summer Session 2",
> > >   "2014-51": "2014  Summer Qtr (COM)",
> > >   "2014-39": "2014  10-wk Summer",
> > >   "2014-25": "2014  Summer Session 1",
> > >   "2014-14": "2014  Spring Quarter",
> > >   "2014-03": "2014  Winter Quarter"
> > > }
> > > ```

---

## /Divisions

```
GET {{url}}/Divisions
```

Returns a list of the possible Divisions mapped to their codes.

---

### Request

>

### Examples:

> **Example: /Divisions**
>
> > ```
> > GET {{url}}/Divisions
> > ```
> >
> > **Request**
> >
> > >
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   "ANY": "Any course division",
> > >   "0xx": "Lower Division only",
> > >   "1xx": "Upper Division only",
> > >   "2xx": "Graduate/Professional only"
> > > }
> > > ```

---

## /class

```
GET {{url}}/Class?Dept=AFAM&CourseNum=40A
```

Returns a list of classes that satisfy the given query params.

---

### Request

> **Query**
>
> | Key       | Value | Description |
> | --------- | ----- | ----------- |
> | Dept      | AFAM  |             |
> | CourseNum | 40A   |             |

### Examples:

> **Example: /class?Dept=PHYSICS&CourseNum=20E**
>
> > ```
> > GET {{url}}/class?Dept=PHYSICS&CourseNum=20E
> > ```
> >
> > **Request**
> >
> > > **Query**
> > >
> > > | Key       | Value   | Description |
> > > | --------- | ------- | ----------- |
> > > | Dept      | PHYSICS |             |
> > > | CourseNum | 20E     |             |
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   "47454": {
> > >     "code": "47454",
> > >     "type": "Lec",
> > >     "sec": "A",
> > >     "units": "4",
> > >     "instructor": "STAFF",
> > >     "time": "TuTh  12:30- 1:50p",
> > >     "place": "RH 104",
> > >     "final": "Fri, Dec 13, 10:30-12:30pm",
> > >     "max": "124",
> > >     "enr": "89",
> > >     "wl": "0",
> > >     "req": "108",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "OPEN"
> > >   },
> > >   "47455": {
> > >     "code": "47455",
> > >     "type": "Dis",
> > >     "sec": "A1",
> > >     "units": "0",
> > >     "instructor": "STAFF/STAFF",
> > >     "time": "Tu 5:00- 5:50p",
> > >     "place": "SH 174",
> > >     "final": "",
> > >     "max": "62",
> > >     "enr": "62",
> > >     "wl": "0",
> > >     "req": "65",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "Waitl"
> > >   },
> > >   "47456": {
> > >     "code": "47456",
> > >     "type": "Dis",
> > >     "sec": "A2",
> > >     "units": "0",
> > >     "instructor": "STAFF/STAFF",
> > >     "time": "Th 5:00- 5:50p",
> > >     "place": "SH 128",
> > >     "final": "",
> > >     "max": "62",
> > >     "enr": "27",
> > >     "wl": "0",
> > >     "req": "29",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "OPEN"
> > >   }
> > > }
> > > ```
>
> **Example: /class?Dept=AFAM&CourseNum=40A**
>
> > ```
> > GET {{url}}/class?Dept=AFAM&CourseNum=40A
> > ```
> >
> > **Request**
> >
> > > **Query**
> > >
> > > | Key       | Value | Description |
> > > | --------- | ----- | ----------- |
> > > | Dept      | AFAM  |             |
> > > | CourseNum | 40A   |             |
> >
> > ---
> >
> > **Response**
> >
> > > **Body**
> > >
> > > ```
> > > {
> > >   "20240": {
> > >     "code": "20240",
> > >     "type": "Lec",
> > >     "sec": "A",
> > >     "units": "4",
> > >     "instructor": "MURILLO, J.",
> > >     "time": "MWF 2:00- 2:50p",
> > >     "place": "PCB 1100",
> > >     "final": "Fri, Dec 13, 1:30-3:30pm",
> > >     "max": "180",
> > >     "enr": "180",
> > >     "wl": "7",
> > >     "req": "250",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "Waitl"
> > >   },
> > >   "20241": {
> > >     "code": "20241",
> > >     "type": "Dis",
> > >     "sec": "1",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F 1:00- 1:50p",
> > >     "place": "HH 226",
> > >     "final": "",
> > >     "max": "30",
> > >     "enr": "30",
> > >     "wl": "4",
> > >     "req": "33",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "Waitl"
> > >   },
> > >   "20242": {
> > >     "code": "20242",
> > >     "type": "Dis",
> > >     "sec": "2",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F  10:00-10:50 ",
> > >     "place": "SST 238",
> > >     "final": "",
> > >     "max": "30",
> > >     "enr": "30",
> > >     "wl": "2",
> > >     "req": "37",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "Waitl"
> > >   },
> > >   "20243": {
> > >     "code": "20243",
> > >     "type": "Dis",
> > >     "sec": "3",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F  12:00-12:50p",
> > >     "place": "SST 238",
> > >     "final": "",
> > >     "max": "30",
> > >     "enr": "30",
> > >     "wl": "1",
> > >     "req": "33",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "Waitl"
> > >   },
> > >   "20244": {
> > >     "code": "20244",
> > >     "type": "Dis",
> > >     "sec": "4",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F  11:00-11:50 ",
> > >     "place": "SST 238",
> > >     "final": "",
> > >     "max": "30",
> > >     "enr": "30",
> > >     "wl": "1",
> > >     "req": "29",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "Waitl"
> > >   },
> > >   "20245": {
> > >     "code": "20245",
> > >     "type": "Dis",
> > >     "sec": "5",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F 2:00- 2:50p",
> > >     "place": "SST 238",
> > >     "final": "",
> > >     "max": "0",
> > >     "enr": "0",
> > >     "wl": "n/a",
> > >     "req": "4",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "FULL"
> > >   },
> > >   "20246": {
> > >     "code": "20246",
> > >     "type": "Dis",
> > >     "sec": "6",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F 3:00- 3:50p",
> > >     "place": "SST 238",
> > >     "final": "",
> > >     "max": "30",
> > >     "enr": "30",
> > >     "wl": "4",
> > >     "req": "32",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "Waitl"
> > >   },
> > >   "20247": {
> > >     "code": "20247",
> > >     "type": "Dis",
> > >     "sec": "7",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F 4:00- 4:50p",
> > >     "place": "HICF 100L",
> > >     "final": "",
> > >     "max": "30",
> > >     "enr": "21",
> > >     "wl": "0",
> > >     "req": "26",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "OPEN"
> > >   },
> > >   "20248": {
> > >     "code": "20248",
> > >     "type": "Dis",
> > >     "sec": "8",
> > >     "units": "0",
> > >     "instructor": "STAFF/MURILLO, J.",
> > >     "time": "F 2:00- 2:50p",
> > >     "place": "HICF 100L",
> > >     "final": "",
> > >     "max": "0",
> > >     "enr": "0",
> > >     "wl": "n/a",
> > >     "req": "0",
> > >     "nor": "0",
> > >     "rstr": "",
> > >     "status": "FULL"
> > >   }
> > > }
> > > ```

---

---

Author: [Zachary Pinto](https://github.com/zpinto)
