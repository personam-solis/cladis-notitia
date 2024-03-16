# **Cladis Notitia**

**Cladis Notitia** is latin for "Disaster Information"

Using publicly available data, gather information on natural disasters world-wide into a single repository.
Data is gathered from multiple sources, parsed, then displayed as statistics.

<br>

<br>

## **Data Sources**

Below are the data sources, how the data is obtained, and the current licensing or terms of use information.

| Source Name | Source Description | Method | Link | License/Terms |
|-------------|--------------------|--------|------|---------------|
| **FEMA** | OpenFEMA is the public’s resource data on multiple aspects of emergency management | API | [OpenFEMA](https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2) | [Pulbic Data](https://www.fema.gov/about/openfema/terms-conditions) |
| **GDACS** | GDACS is a cooperation framework between the United Nations, the European Commission and disaster managers worldwide to improve alerts, information exchange and coordination in the first phase after major sudden-onset disasters. | [XML File Download](https://gdacs.org/xml/rss.xml) | [GDACS](https://gdacs.org/) | [Professional, not general use](https://gdacs.org/About/termofuse.aspx) |
| **EM-DAT** | EM-DAT contains data on the occurrence and impacts of over 26,000 mass disasters worldwide from 1900 to the present day. The database is compiled from various sources, including UN agencies, non-governmental organizations, reinsurance companies, research institutes, and press agencies | XLSX File Download | [EM-DAT](https://www.emdat.be/) | [Non-commercial Use](https://doc.emdat.be/docs/legal/terms-of-use/) |

<br>

### Disclaimers

**FEMA:**

Federal Emergency Management Agency (FEMA), OpenFEMA Dataset: Disaster Declarations Summaries - v2. This product uses the FEMA OpenFEMA API, but is not endorsed by FEMA. The Federal Government or FEMA cannot vouch for the data or analyses derived from these data after the data have been retrieved from the Agency's website(s).

<br>

**GDACS:**

THE GDACS STAKEHOLDERS AND ADVISORY BOARD (INCLUDING BUT NOT LIMITED TO THE EUROPEAN COMMISSION, UN-OCHA AND UNOSAT) DO NOT ASSUME ANY RESPONSIBILITY OR LIABILITY WHATSOEVER WITH REGARD TO THE INFORMATION ON THIS SITE AND WILL NOT BE LIABLE FOR ANY DAMAGE OR LOSS OF LIFE THAT MIGHT RESULT FROM THE USE OF ITS CONTENTS.

<br>

**EM-DAT:**

The CRED makes every effort to ensure, but cannot and does not guarantee, and makes no warranties as to, the accuracy, accessibility, integrity, and timeliness of this information. The CRED assumes no liability or responsibility for any errors or omissions in the content of this site and further disclaims any liability of any nature for any loss, howsoever caused, in connection with using EM-DAT. The CRED may make changes to EM-DAT at any time without notice. If you are undertaking an in-depth analysis, we recommend that you consult our staff to obtain a good understanding of the weaknesses, limitations, and peculiarities of our data;

<br>

### **Data Source Attributes**

These are all the relevant attributes from all data sources along with a brief description.

**FEMA:**
* `state` - X
* `declarationDate` - Date of entry (YYYY-MM-DD`T`hh:mm:ss.nnn`Z`)
* `incidentType` - The type of incident (Fire, Flood)
* `incidentBeginDate` - Start date of disaster (YYYY-MM-DD`T`hh:mm:ss.nnn`Z`)
* `incidentEndDate` - End date of disaster (YYYY-MM-DD`T`hh:mm:ss.nnn`Z`)

<br>

**GDACS:**
* `gdacs:dateadded` - When the entry was first recorded (DOW, DD Mmm YYYY HH:MM:SS TZ)
* `gdacs:datemodified` - When the record was updated (DOW, DD Mmm YYYY HH:MM:SS TZ)
* `gdacs:fromdate` - Start date of disaster (DOW, DD Mmm YYYY HH:MM:SS TZ)
* `gdacs:todate` - End date of disaster (DOW, DD Mmm YYYY HH:MM:SS TZ)
* `geo:lat` - Latitude location in Decimal Degrees
* `geo:long` - Longitude location in Decimal Degrees
* `gdacs:eventtype` - GDACS Code for the event (requires reference)
* `gdacs:severity` - Severity unit of measurement and value
* `gdacs:iso3` - Three digit Country Name (ISO3)
* `gdacs:country` - Name of Country
* `gdacs:population` - Population affected by the disaster

<br>

**EM-DAT:**
* `Disaster Group` - Natural Disaster or not
* `Disaster Subgroup` - Disaster Group Subtype (Geophysical, Hydrological, Climatological)
* `Disaster Type` - The Major Type of disaster (Drought, Flood, Storm, Earthquake)
* `Disaster Subtype` - The specific disaster type (Land Fire, Cold wave, Tropical Cyclone)
* `ISO` - Three digit Country Name (ISO3)
* `Country` - Name of Country
* `Location` - Description of location
* `Magnitude` - Severity of the disaster as an integer or floating point
* `Magnitude Scale` - The unit of measurement for the disaster (Richter, Kph, Vaccinated)
* `Latitude` - Latitude location in Decimal Degrees
* `Longitude` - Longitude location in Decimal Degrees
* `Start Year` - Year (YYYY)
* `Start Month` - Month (M)
* `Start Day` - Day (D)
* `End Year` - Year (YYYY)
* `End Month` - Month (M)
* `End Day` - Day (D)
* `Total Deaths` - Total number of lives lost during the disaster
* `Total Affected` - Number of people that were injured affected, and homeless
* `Reconstruction Costs ('000 US$)` - Costs in USD to rebuild
* `Entry Date` - When the entry was first recorded (YYYY-MM-DD)
* `Last Update` - When the record was updated (YYYY-MM-DD)

<br>

<br>

## **Python Packages**

Below are the packages that were installed outside the standard Python library

* `requests`
* `pandas`
