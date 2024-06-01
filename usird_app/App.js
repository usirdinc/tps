import React, { useState } from 'react';
import { TextField, Button, FormControl, InputLabel, Select, MenuItem, IconButton, Box, Grid, Tabs, Tab, Divider } from '@mui/material';
import { TabContext, TabPanel } from '@mui/lab';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';

window.document.title = "TPS FORM"

const initialFormData = {
  personalInformation: {
    name: '',
    othernames: '',
    othernames_2: [''],
    alienNumber: '',
    uscisAccountNumber: '',
    dateOfBirth: '',
    otherDatesOfBirth: '',
    otherDatesOfBirth_2: [''],
    gender: '',
    cityOfBirth: '',
    countryOfBirth: '',
    physicalAddress: {
      streetName: '',
      aptType: '',
      apartmentNumber: '',
      city: '',
      province: '',
      state: '',
      zipCode: '',
      country: ''
    },
    countriesOfResidence: [''],
    countryOfNationality: [''],
    height: { feet: 0, inch: 0 },
    weight: 0,
    race: '',
    religion: '',
    maritalStatus: '',
    children: '',
    mobileNumber: '',
    emailAddress: ''
  },
  travel: {
    dateOfLastEntry: '',
    immigrationStatus: '',
    portOfEntry: '',
    cityOfEntry: '',
    stateOfEntry: '',
    i94Number: '',
    authorizedPeriodOfStay: '',
    passportNumber: '',
    travelDocumentNumber: '',
    expirationOfPassport: '',
    additionalPassport: '',
    additionalPassport_2: [''],
  },
  parents: {
    mother: {
      name: '',
      bornAndRaised: ''
    },
    father: {
      name: '',
      bornAndRaised: ''
    }
  },
  spouse: {
    uscisAccountNumber: '',
    aNumber: '',
    name: '',
    mailingAddress: {
      streetName: '',
      aptType: '',
      apartmentNumber: '',
      city: '',
      province: '',
      state: '',
      zipCode: '',
      country: ''
    },
    dateOfBirth: '',
    marriage: {
      dateOfMarriage: '',
      placeOfMarriage: '',
      city: '',
      state: '',
      province: '',
      country: ''
    },
    tps: {
      spouseHadTPS: '',
      dateFrom: '',
      dateTo: '',
      present: false,
      tpsValid: ''
    }
  },
  formerSpouses: [
    { name: '', nationality: '', aNumber: '', dateOfBirth: '', dateOfDeath: '', dateFrom: '', dateTo: '', howMarriageEnded: '', spouseHadTPS: '', tps: { dateFrom: '', dateTo: '', tpsValid: '' } }
  ],
  children: [],
};

const states = [
  'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
  'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
  'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
  'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
  'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
];

const DynamicForm = () => {
  const [formData, setFormData] = useState(initialFormData);
  const [tabValue, setTabValue] = useState('1');

  const handleInputChange = (section, field, value) => {
    setFormData(prevState => ({
      ...prevState,
      [section]: {
        ...prevState[section],
        [field]: value
      }
    }));
  };  

  const handleNestedInputChange = (section, subSection, field, value) => {
    setFormData(prevState => ({
      ...prevState,
      [section]: {
        ...prevState[section],
        [subSection]: {
          ...prevState[section][subSection],
          [field]: value
        }
      }
    }));
  };

  const handleArrayInputChange = (section, index, field, value) => {
    const updatedArray = [...formData[section]];
    updatedArray[index] = {
      ...updatedArray[index],
      [field]: value
    };
    setFormData(prevState => ({
      ...prevState,
      [section]: updatedArray
    }));
  };  

  const handleAddItem = (section, subSection, newItem) => {
    setFormData((prevState) => {
      if (subSection) {
        // Handling nested array case
        const updatedSubSection = Array.isArray(prevState[section][subSection])
         ? [...prevState[section][subSection], newItem]
          : [newItem];
        return {
         ...prevState,
          [section]: {
           ...prevState[section],
            [subSection]: updatedSubSection,
          },
        };
      } else {
        // Handling non-nested array case
        const updatedSection = Array.isArray(prevState[section])
         ? [...prevState[section], newItem]
          : [newItem];
        return {
         ...prevState,
          [section]: updatedSection,
        };
      }
    });
  };

  const handleAddFormerSpouse = () => {
    const newFormerSpouse = {
      name: '',
      nationality: '',
      aNumber: '',
      dateOfBirth: '',
      dateOfDeath: '',
      dateFrom: '',
      dateTo: '',
      howMarriageEnded: '',
      spouseHadTPS: '',
      tps: {
        dateFrom: '',
        dateTo: '',
        tpsValid: ''
      }
    };
  
    setFormData(prevState => ({
      ...prevState,
      formerSpouses: [...prevState.formerSpouses, newFormerSpouse]
    }));
  };
  

  const handleRemoveItem = (section, subSection, index) => {
    setFormData(prevState => {
      if (subSection) {
        // Handling nested array case
        const updatedSubSection = [...prevState[section][subSection]];
        updatedSubSection.splice(index, 1);
  
        return {
          ...prevState,
          [section]: {
            ...prevState[section],
            [subSection]: updatedSubSection,
          }
        };
      } else {
        // Handling non-nested array case
        const updatedSection = [...prevState[section]];
        updatedSection.splice(index, 1);
  
        return {
          ...prevState,
          [section]: updatedSection,
        };
      }
    });
  };  

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  const renderFormerSpouses = () => {
    return (
      <>
        <Grid container item spacing={2} xs={12} lg={6} margin="auto" >  
          {Array.isArray(formData.formerSpouses) && formData.formerSpouses.map((formerSpouse, index) => (
            <>   
              <Grid xs={12}>
                <Divider>
                  <h2>Former Spouse {index + 1}</h2>
                </Divider>
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, 'name', 'Name')}
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, `nationality`, 'Nationality')}
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, `aNumber`, 'Alien Number (if applicable)')}
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, `dateOfBirth`, 'Date of Birth')}
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, `dateOfDeath`, 'Date of Death (if applicable)')}
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, `dateFrom`, 'Date of Marriage: From', 'date')}
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, `dateTo`, 'Date of Marriage: To', 'date')}
              </Grid>
              <Grid item xs={12} md={6} sm={4}>
                {renderInput(`formerSpouses[${index}]`, `howMarriageEnded`, 'How Marriage Ended')}
              </Grid>
              <Grid item xs={12} md={6} sm={8}>
                {renderDropdown(`formerSpouses[${index}`, `spouseHadTPS`, 'Does your spouse hold TPS before?', ['Yes, he/she holds TPS', 'No, he/she does not hold any TPS'])}
              </Grid>
              {renderDynamicSection(`formerSpouses.formerSpouse${index}`, `spouseHadTPS`, () => (
                <>
                  <Grid item xs={12}>
                    {renderDropdown(`formerSpouses.formerSpouse${index}`, `tps.tpsValid`, 'Is his/her TPS Status still valid?', ['Yes, it is still valid until present', 'No, it is not valid anymore'])}
                  </Grid>
                  {renderDynamicSection(`formerSpouses.formerSpouse${index}`, `tps.tpsValid`, () => (
                    <>
                      <Grid item xs={12} sm={6} md={4}>
                        {renderInput(`formerSpouses.formerSpouse${index}`, `tps.dateFrom`, 'TPS Valid Date From', 'date')}
                      </Grid>
                      <Grid item xs={12} sm={6} md={4}>
                        {renderInput(`formerSpouses.formerSpouse${index}`, `tps.dateTo`, 'TPS Valid Date To', 'date')}
                      </Grid>
                    </>
                  ))}
                </>
              ))}
              <Grid xs={12} margin={2}>
                <IconButton onClick={() => handleRemoveItem('formerSpouses', null, index)} aria-label="delete">
                  <DeleteIcon />
                </IconButton>
              </Grid>
            </>
        ))}
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={handleAddFormerSpouse}
            style={{ float: 'right' }}
            >
            Add Former Spouse
          </Button>
        </Grid>
        {renderNavigationButtons()}
      </Grid>
    </>
  );
};
  

  const renderInput = (section, field, label, type = 'text') => (
    <Box mb={2}>
      <TextField
        label={label}
        type={type}
        value={formData[section][field]}
        onChange={(e) => handleInputChange(section, field, e.target.value)}
        fullWidth
        InputLabelProps={{ shrink: true }}
      />
    </Box>
  );

  const renderNestedInput = (section, subSection, field, label, type = 'text') => (
    <Box mb={2}>
      <TextField
        label={label}
        type={type}
        value={formData[section][subSection][field]}
        onChange={(e) => handleNestedInputChange(section, subSection, field, e.target.value)}
        fullWidth
        InputLabelProps={{ shrink: true }}
      />
    </Box>
  );

  const renderArrayInput = (section, subSection, index, label) => (
    <Box display="flex" alignItems="center" mb={2}>
      <TextField
        label={label}
        type="text"
        value={formData[section][subSection][index]}
        onChange={(e) => handleArrayInputChange(section, index, subSection, e.target.value)}
        fullWidth
        InputLabelProps={{ shrink: true }}
      />
      <IconButton onClick={() => handleRemoveItem(section, subSection, index)} aria-label="delete">
        <DeleteIcon />
      </IconButton>
      {index === formData[section][subSection].length - 1 && ( // Add this condition
        <IconButton onClick={() => handleAddItem(section, subSection, '')} aria-label="add">
          <AddIcon />
        </IconButton>
      )}
    </Box>
  );
  

  const renderDropdown = (section, field, label, options) => (
    <FormControl fullWidth>
      <InputLabel shrink style={{ overflow: "hidden", background: "white", padding: "0 10px" }}>{label}</InputLabel>
      <Select
        value={formData[section][field]}
        onChange={(e) => handleInputChange(section, field, e.target.value)}
      >
        <MenuItem value="" disabled>{label}</MenuItem>
        {Array.isArray(options) ? options.map((option, index) => (
          <MenuItem key={index} value={option}>{option}</MenuItem>
        )) : null}
      </Select>
    </FormControl>
  );

  const renderDynamicSection = (section, field, renderContent) => (
    String(formData[section][field]).split(",")[0] === 'Yes' && renderContent()
  );

  const renderDynamicSpacing = (section, field) => (
    String(formData[section][field].split(",")[0]) === 'Yes'
  )

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(JSON.stringify(formData, null, 2));
  };

  let [tabCount, setTabCount] = useState(3);

  const renderNavigationButtons = () => (
    <Box display="flex" justifyContent="flex-end" mt={5}>
      {tabValue !== tabCount && (
        <Button
          variant="contained"
          color="primary"
          onClick={() => setTabValue((prev) => (parseInt(prev) + 1).toString())}
        >
          Next
        </Button>
      )}
      {tabValue === tabCount && (
        <Button
          type="submit"
          variant="contained"
          color="primary"
        >
          Submit
        </Button>
      )}
    </Box>
  );

  return (
    <form onSubmit={handleSubmit} style={{ width: '90%', margin: 'auto' }}>
      <TabContext value={tabValue}>
        <Tabs value={tabValue} onChange={handleTabChange} aria-label="form tabs">
          <Tab label="Personal Information" value="1" />
          <Tab label="Travel" value="2" />
          <Tab label="Spouse" value="3" />
          {/* {String(formData['personalInformation']['maritalStatus']) === 'Married' && (
          )} */}
            <Tab label="Former Spouses" value="4" />
          {/* {String(formData['personalInformation']['maritalStatus']) === 'Divorced' && (
          )} */}
          <Tab label="Children" value="5" />
          <Tab label="Review & Submit" value="6" />
        </Tabs>
        <TabPanel value="1">
          <Grid container item spacing={2} rowGap={1} xs={12} lg={6} margin="auto" alignContent="center">
            <Grid item xs={12} sm={8} md={8}>
              {renderInput('personalInformation', 'name', 'Name')}
            </Grid>
            <Grid item xs={12} sm={4} md={4}>
              {renderDropdown('personalInformation', 'othernames', 'Do you have other names', ['Yes, I have other name(s).', 'No, I don\'t have other names'])}
            </Grid>
            <Grid item xs={12} style={{ "display": renderDynamicSpacing('personalInformation', 'othernames') ? "block" : "none" }}>
              {renderDynamicSection('personalInformation', 'othernames', () => (
                <>
                  {formData.personalInformation.othernames_2.map((othername, index) => (
                    <div key={index}>
                      {renderArrayInput('personalInformation', 'othernames_2', index, `Other Name ${index + 1}`)}
                    </div>
                  ))}
                </>
              ))}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderDropdown('personalInformation', 'gender', 'Gender', ['Male', 'Female'])}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('personalInformation', 'race', 'Race')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('personalInformation', 'religion', 'Religion')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderDropdown('personalInformation', 'maritalStatus', 'Marital Status', ['Single', 'Married', 'Divorced', 'Widowed'])}
            </Grid>
            <Grid item xs={12} sm={6} md={8}>
              {renderDropdown('personalInformation', 'children', 'Do you have a child?', ['Yes, I have a child', 'No, I don\'t have any child'])}
            </Grid>
            <Grid item xs={12} sm={6}>
              {renderInput('personalInformation', 'dateOfBirth', 'Date of Birth', 'date')}
            </Grid>
            <Grid item xs={12} sm={6}>
              {renderInput('personalInformation', 'cityOfBirth', 'City of Birth')}
            </Grid>
            <Grid item xs={12} sm={6}>
              {renderInput('personalInformation', 'countryOfBirth', 'Country of Birth')}
            </Grid>
            <Grid item xs={12} sm={6}>
              {renderDropdown('personalInformation', 'otherDatesOfBirth', 'Do you have other dates of birth?', ['Yes, I have other date(s) of birth.', 'No, I don\'t have other dates of birth.'])}
            </Grid>
            <Grid item xs={12}>
              {renderDynamicSection('personalInformation', 'otherDatesOfBirth', () => (
                <>
                  {formData.personalInformation.otherDatesOfBirth_2.map((otherDateOfBirth, index) => (
                    <div key={index}>
                      {renderArrayInput('personalInformation', 'otherDatesOfBirth_2', index, `Other Date Of Birth ${index + 1}`)}
                    </div>
                  ))}
                </>
              ))}
            </Grid>
            <Grid item container xs={12} spacing={2}>
              <Grid item xs={12} sm={8}>
                {renderInput('parents', 'mother.name', 'Mother\'s Name')}
              </Grid>
              <Grid item xs={12} sm={4}>
                {renderInput('parents', 'mother.bornAndRaised', 'City of Residence')}
              </Grid>
              <Grid item xs={12} sm={8}>
                {renderInput('parents', 'father.name', 'Father\'s Name')}
              </Grid>
              <Grid item xs={12} sm={4}>
                {renderInput('parents', 'father.bornAndRaised', 'City of Residence')}
              </Grid>
            </Grid>
            <Grid item xs={12}>
              <Divider fullWidth>
                <h3>Contact Information</h3>
              </Divider>
            </Grid>
            <Grid item xs={12} sm={4}>
              {renderInput('personalInformation', 'dayPhoneNumber', 'Day Phone Number')}
            </Grid>
            <Grid item xs={12} sm={8}>
              {renderInput('personalInformation', 'emailAddress', 'Email Address')}
            </Grid>
            <Grid item xs={12} sm={6} md={2}>
              {renderDropdown('personalInformation', 'aptType', 'Apartment Type', ['Apartment', 'Suite', 'Floor'])}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderNestedInput('personalInformation', 'physicalAddress', 'apartmentNumber', 'Apartment Number')}
            </Grid>
            <Grid item xs={12} sm={6} md={6}>
              {renderNestedInput('personalInformation', 'physicalAddress', 'streetName', 'Street Name')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderNestedInput('personalInformation', 'physicalAddress', 'city', 'City')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderNestedInput('personalInformation', 'physicalAddress', 'province', 'Province')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderDropdown('personalInformation', 'state', 'State', states)}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderNestedInput('personalInformation', 'physicalAddress', 'zipCode', 'Zip Code')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderNestedInput('personalInformation', 'physicalAddress', 'country', 'Country')}
            </Grid>
            <Grid item xs={12}>
              <Divider fullWidth>
                <h3>List of Countries of Residence</h3>
              </Divider>
            </Grid>
            <Grid item xs={12} margin="auto">
              {formData.personalInformation.countriesOfResidence.map((country, index) => (
                <div key={index}>
                  {renderArrayInput('personalInformation', 'countriesOfResidence', index, `Country of Residence`)}
                </div>
              ))}
            </Grid>
            <Grid item xs={12} margin="auto">
              {formData.personalInformation.countryOfNationality.map((country, index) => (
                <div key={index}>
                  {renderArrayInput('personalInformation', 'countryOfNationality', index, 'Country of Nationality')}
                </div>
              ))}
            </Grid>
          {renderNavigationButtons()}
          </Grid>
        </TabPanel>
        <TabPanel value="2">
          <Grid container item spacing={2} xs={12} lg={6} margin="auto">
            <Grid item xs={12}>
              <Divider fullWidth>
                <h3>Travel Information</h3>
              </Divider>
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('personalInformation', 'alienNumber', 'Alien Number (if applicable)')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('personalInformation', 'uscisAccountNumber', 'USCIS Account Number (if applicable)')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderDropdown('personalInformation', 'immigrationStatus', 'Visa Category', ['B1 - Business Visitor Visa', 'B2 - Tourist Visitor Visa', 'C1 - Transit Visa', 'D1 - Crew Member Visa', 'EB5 - Immigrant Investor Visa', 'F1 - Student Visa', 'K1 - Fiance Visa'])}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'dateOfLastEntry', 'Date of Last Entry', 'date')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'i94Number', 'I-94 Number')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'authorizedPeriodOfStay', 'Authorized Period of Stay')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'portOfEntry', 'Airport of Entry')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'cityOfEntry', 'City of Entry')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'stateOfEntry', 'State of Entry')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'travelDocumentNumber', 'Travel Document Number')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'passportNumber', 'Passport Number')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('travel', 'expirationOfPassport', 'Expiration of Passport', 'date')}
            </Grid>
            <Grid item xs={12}>
              {renderDropdown('travel', 'additionalPassport', 'Additional Passport', ['Yes, I have additional passport', 'No, I don\'t have additional passport.'])}
            </Grid>
            <Grid item xs={12} style={{ "display": renderDynamicSpacing('travel', 'additionalPassport') ? "block" : "none" }}>
              {renderDynamicSection('travel', 'additionalPassport', () => (
                <>
                  {formData.travel.additionalPassport_2.map((additional_passport, index) => (
                    <div key={index}>
                      {renderArrayInput('travel', 'additionalPassport_2', index, 'Additional Passport')}
                    </div>
                  ))}
                  <Button style={{ "float": "right", "marginRight": "20px" }} variant="contained" color="primary" onClick={() => handleAddItem('travel', 'additionalPassport_2', '')}>
                    Add Passport
                  </Button>
                </>
              ))}
            </Grid>
          {renderNavigationButtons()}
          </Grid>
        </TabPanel>
        <TabPanel value="3">
          <Grid container item spacing={2} xs={12} lg={6} margin="auto">
            <Grid xs={12}>
              <Divider>
                <h2>Spouse Information</h2>
              </Divider>
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'uscisAccountNumber', 'USCIS Account Number (if applicable)')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'aNumber', 'Alien Number (if applicable)')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'name', 'Name')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'dateOfBirth', 'Date of Birth', 'date')}
            </Grid>
            <Grid item xs={12} sm={6} md={8}>
              {renderDropdown('spouse', 'tps.spouseHadTPS', 'Does your spouse hold TPS before?', ['Yes, he/she holds TPS', 'No, he/she does not hold any TPS'])}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'marriage.dateOfMarriage', 'Date of Marriage', 'date')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'marriage.placeOfMarriage', 'Place of Marriage')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'marriage.city', 'City of Marriage')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'marriage.state', 'State of Marriage')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'marriage.province', 'Province of Marriage')}
            </Grid>
            <Grid item xs={12} sm={6} md={4}>
              {renderInput('spouse', 'marriage.country', 'Country of Marriage')}
            </Grid>

            {renderDynamicSection('spouse', 'tps.spouseHadTPS', () => (
              <>
                <Grid item xs={12}>
                  {renderDropdown('spouse', 'tps.tpsValid', 'Is his/her TPS Status still valid?', ['Yes, it is still valid until present', 'No, it is not valid anymore'])}
                </Grid>
                {renderDynamicSection('spouse', 'tps.tpsValid', () => (
                  <>
                    <Grid item xs={12} sm={6} md={4}>
                      {renderInput('spouse', 'tps.dateFrom', 'TPS Valid Date From', 'date')}
                    </Grid>
                    <Grid item xs={12} sm={6} md={4}>
                      {renderInput('spouse', 'tps.dateTo', 'TPS Valid Date To', 'date')}
                    </Grid>
                  </>
                ))}
              </>
            ))}
          {renderNavigationButtons()}
          </Grid>
        </TabPanel>
          <TabPanel value="4">
            {renderFormerSpouses()}
          </TabPanel>
        {/* {String(formData['personalInformation']['maritalStatus']) === 'Divorced' && (
        
        )} */}
        <TabPanel value="5">
          <h2>Children</h2>
          <Grid container spacing={2} xs={12} lg={6} margin="auto">
            {formData.children.map((child, index) => (
              <div key={index}>
                {renderNestedInput('children', index, 'name', 'Child Name')}
                {renderNestedInput('children', index, 'uscisAccountNumber', 'Child USCIS Account Number')}
                {renderNestedInput('children', index, 'aNumber', 'Child A Number')}
                {renderNestedInput('children', index, 'dateOfBirth', 'Child Date of Birth')}
                {renderNestedInput('children', index, 'mailingAddress', 'streetName', 'Child Street Name')}
                {renderNestedInput('children', index, 'mailingAddress', 'aptType', 'Child Apt Type')}
                {renderNestedInput('children', index, 'mailingAddress', 'apartmentNumber', 'Child Apartment Number')}
                {renderNestedInput('children', index, 'mailingAddress', 'city', 'Child City')}
                {renderNestedInput('children', index, 'mailingAddress', 'province', 'Child Province')}
                {renderNestedInput('children', index, 'mailingAddress', 'state', 'Child State')}
                {renderNestedInput('children', index, 'mailingAddress', 'zipCode', 'Child Zip Code')}
                {renderNestedInput('children', index, 'mailingAddress', 'country', 'Child Country')}
                <IconButton onClick={() => handleRemoveItem('children', '', index)} aria-label="delete">
                  <DeleteIcon />
                </IconButton>
              </div>
            ))}
            <Button variant="contained" color="primary" onClick={() => handleAddItem('children', '', { name: '', uscisAccountNumber: '', aNumber: '', dateOfBirth: '', mailingAddress: { streetName: '', aptType: '', apartmentNumber: '', city: '', province: '', state: '', zipCode: '', country: '' } })}>
              Add Child
            </Button>
            {renderNavigationButtons()}
          </Grid>
        </TabPanel>
        <TabPanel value="6">
          <h2>Review & Submit</h2>
          <pre>{JSON.stringify(formData, null, 2)}</pre>
          {renderNavigationButtons()}
        </TabPanel>
      </TabContext>
    </form>
  );
};

export default DynamicForm;
