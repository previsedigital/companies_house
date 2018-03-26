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
 |  get_company(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the basic company information
 |      :param company_number:
 |  
 |  get_company_charges(self, company_number:str, charge_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get a single charge for a company
 |      :param company_number:
 |      :param charge_id:
 |  
 |  get_company_exemptions(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the company exemptions information.
 |      :param company_number:
 |  
 |  get_company_filing_history(self, company_number:str, transaction_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the filing history of the company
 |      :param company_number:
 |      :param transaction_id:
 |  
 |  get_company_insolvency(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get company insolvency information
 |      :param company_number:
 |  
 |  get_company_persons_with_significant_control_corporate_entity(self, company_number:str, psc_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the corporate entity with significant control
 |      :param company_number:
 |      :param psc_id:
 |  
 |  get_company_persons_with_significant_control_individual(self, company_number:str, psc_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the individual person with significant control
 |      :param company_number:
 |      :param psc_id:
 |  
 |  get_company_persons_with_significant_control_legal_person(self, company_number:str, psc_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the legal person with significant control
 |      :param company_number:
 |      :param psc_id:
 |  
 |  get_company_persons_with_significant_control_statements(self, company_number:str, statement_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the person with significant control statement
 |      :param company_number:
 |      :param statement_id:
 |  
 |  get_company_persons_with_significant_control_super_secure(self, company_number:str, super_secure_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the super secure person with significant control
 |      :param company_number:
 |      :param super_secure_id:
 |  
 |  get_company_registered_office_address(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the current address of a company
 |      :param company_number:
 |  
 |  get_company_registers(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the company registers information
 |      :param company_number:
 |  
 |  get_disqualified_officers_corporate(self, officer_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get a corporate officer's disqualifications
 |      :param officer_id:
 |  
 |  get_disqualified_officers_natural(self, officer_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get a natural officer's disqualifications
 |      :param officer_id:
 |  
 |  list_company_charges(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get a list of charges for a company
 |      :param company_number:
 |  
 |  list_company_filing_history(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get the filing history of the company
 |      :param company_number:
 |  
 |  list_company_officers(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      List the company officers
 |      :param company_number:
 |  
 |  list_company_persons_with_significant_control(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      List the company persons with significant control
 |      :param company_number:
 |  
 |  list_company_persons_with_significant_control_statements(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      List the company persons with significant control statements
 |      :param company_number:
 |  
 |  list_company_uk_establishments(self, company_number:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Get a list of UK Establishment companies
 |      :param company_number:
 |  
 |  list_officers_appointments(self, officer_id:str, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      List the officer appointments
 |      :param officer_id:
 |  
 |  search(self, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Search Companies House
 |  
 |  search_companies(self, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Search companies
 |  
 |  search_disqualified_officers(self, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Search disqualified officers
 |  
 |  search_officers(self, flatten:bool=False, **kwargs) -> Union[dict, NoneType]
 |      Search company officers
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from CompaniesHouseAPIBase:
 |  
 |  __init__(self, api_key:str) -> None
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  get(self, query:str, flatten:bool=False) -> Union[dict, NoneType]
 |      Run a GET query against the Companies' House API
 |      :param query: the query, e.g. "company/09117429"
 |      :param flatten: flatten the result dictionary
 |      :return: the result as dict
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
