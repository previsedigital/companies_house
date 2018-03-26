# Companies' House Python API
Simply create an API client as an instance of CompaniesHouseAPI:
```
from companies_house.api import CompaniesHouseAPI
ch = CompaniesHouseAPI(api_key)
```

This will give you access to all the functions registered in the API. For full reference,
refer to [the API documentation](https://developer.companieshouse.gov.uk/api/docs/)
```
help(CompaniesHouseAPI)
```

```
Help on class CompaniesHouseAPI in module api:

class CompaniesHouseAPI(CompaniesHouseAPIBase)
 |  Method resolution order:
 |      CompaniesHouseAPI
 |      CompaniesHouseAPIBase
 |      builtins.object
 |  
 |  Methods defined here:
 |  
 |  company(self, **kwargs) -> Union[dict, NoneType]
 |      Get the basic company information (get)
 |      :param company_number:
 |  
 |  company_charges(self, **kwargs) -> Union[dict, NoneType]
 |      Get a single charge for a company (get)
 |      :param company_number:
 |      :param charge_id:
 |  
 |  company_exemptions(self, **kwargs) -> Union[dict, NoneType]
 |      Get the company exemptions information. (get)
 |      :param company_number:
 |  
 |  company_filing_history(self, **kwargs) -> Union[dict, NoneType]
 |      Get the filing history of the company (list)
 |      :param company_number:
 |  
 |  company_insolvency(self, **kwargs) -> Union[dict, NoneType]
 |      Get company insolvency information (get)
 |      :param company_number:
 |  
 |  company_officers(self, **kwargs) -> Union[dict, NoneType]
 |      List the company officers (list)
 |      :param company_number:
 |  
 |  company_persons_with_significant_control(self, **kwargs) -> Union[dict, NoneType]
 |      List the company persons with significant control (list)
 |      :param company_number:
 |  
 |  company_persons_with_significant_control_corporate_entity(self, **kwargs) -> Union[dict, NoneType]
 |      Get the corporate entity with significant control (get corporate entities)
 |      :param company_number:
 |      :param psc_id:
 |  
 |  company_persons_with_significant_control_individual(self, **kwargs) -> Union[dict, NoneType]
 |      Get the individual person with significant control (get individual)
 |      :param company_number:
 |      :param psc_id:
 |  
 |  company_persons_with_significant_control_legal_person(self, **kwargs) -> Union[dict, NoneType]
 |      Get the legal person with significant control (get legal persons)
 |      :param company_number:
 |      :param psc_id:
 |  
 |  company_persons_with_significant_control_statements(self, **kwargs) -> Union[dict, NoneType]
 |      Get the person with significant control statement (get statement)
 |      :param company_number:
 |      :param statement_id:
 |  
 |  company_persons_with_significant_control_super_secure(self, **kwargs) -> Union[dict, NoneType]
 |      Get the super secure person with significant control (get super secure person)
 |      :param company_number:
 |      :param super_secure_id:
 |  
 |  company_registered_office_address(self, **kwargs) -> Union[dict, NoneType]
 |      Get the current address of a company (get)
 |      :param company_number:
 |  
 |  company_registers(self, **kwargs) -> Union[dict, NoneType]
 |      Get the company registers information (get)
 |      :param company_number:
 |  
 |  company_uk_establishments(self, **kwargs) -> Union[dict, NoneType]
 |      Get a list of UK Establishment companies (list)
 |      :param company_number:
 |  
 |  disqualified_officers_corporate(self, **kwargs) -> Union[dict, NoneType]
 |      Get a corporate officer's disqualifications (Get corporate)
 |      :param officer_id:
 |  
 |  disqualified_officers_natural(self, **kwargs) -> Union[dict, NoneType]
 |      Get a natural officer's disqualifications (Get natural)
 |      :param officer_id:
 |  
 |  officers_appointments(self, **kwargs) -> Union[dict, NoneType]
 |      List the officer appointments (list)
 |      :param officer_id:
 |  
 |  search(self, **kwargs) -> Union[dict, NoneType]
 |      Search Companies House (Search all)
 |  
 |  search_companies(self, **kwargs) -> Union[dict, NoneType]
 |      Search companies (Search company)
 |  
 |  search_disqualified_officers(self, **kwargs) -> Union[dict, NoneType]
 |      Search disqualified officers (Search disqualified officer)
 |  
 |  search_officers(self, **kwargs) -> Union[dict, NoneType]
 |      Search company officers (Search officer)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from CompaniesHouseAPIBase:
 |  
 |  __init__(self, api_key:str) -> None
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  get(self, query:str) -> Union[dict, NoneType]
 |      Run a GET query against the Companies' House API
 |      :param query: the query, e.g.
 |      :return:
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from CompaniesHouseAPIBase:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from CompaniesHouseAPIBase:
 |  
 |  __annotations__ = {'_api_key': <class 'str'>}


```
When the API has changed, 
run `update.py` to re-download the API definition. 
When running the API, this documentation is updated automatically.
