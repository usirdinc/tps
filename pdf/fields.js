const formI821 = [
    // Part 1: Information About You
    { type: 'text', label: 'Current Legal Name', name: 'currentLegalName', fields: ['First name', 'Middle name', 'Last name'] },
    { type: 'text', label: 'Other Names Used', name: 'otherNamesUsed', fields: ['First name', 'Middle name', 'Last name'] },
    { type: 'address', label: 'U.S. Mailing Address', name: 'usMailingAddress' },
    { type: 'address', label: 'U.S. Physical Address', name: 'usPhysicalAddress' },
    { type: 'date', label: 'Date of Birth', name: 'dateOfBirth' },
    { type: 'text', label: 'Country of Birth', name: 'countryOfBirth' },
    { type: 'text', label: 'Country of Citizenship or Nationality', name: 'countryOfCitizenship' },
    { type: 'text', label: 'Alien Registration Number (A-Number)', name: 'aNumber' },
    { type: 'text', label: 'USCIS Online Account Number', name: 'uscisOnlineAccountNumber' },
    { type: 'date', label: 'Date of Entry into the U.S.', name: 'dateOfEntry' },
    { type: 'text', label: 'Immigration Status at Entry', name: 'immigrationStatusAtEntry' },
    { type: 'text', label: 'Current Immigration Status', name: 'currentImmigrationStatus' },
  
    // Part 2: Application Type
    { type: 'radio', label: 'Application Type', name: 'applicationType', options: ['Initial application', 'Re-registration', 'Late initial application'] },
  
    // Part 3: Information About Your Eligibility
    { type: 'text', label: 'Basis for Your Eligibility for TPS', name: 'eligibilityBasis' },
    { type: 'text', label: 'Country Designated for TPS', name: 'tpsCountry' },
    { type: 'date', label: 'Date of Last Entry into the U.S.', name: 'lastEntryDate' },
    { type: 'text', label: 'Current Immigration Status', name: 'currentStatus' },
    { type: 'textarea', label: 'Other Applications or Petitions Filed with USCIS', name: 'otherApplications' },
    { type: 'textarea', label: 'Criminal History', name: 'criminalHistory' },
    { type: 'textarea', label: 'Previous TPS Applications', name: 'previousTpsApplications' },
  
    // Part 4: Information About Your Residence and Travel
    { type: 'text', label: 'Current Physical Presence in the U.S.', name: 'physicalPresence' },
    { type: 'textarea', label: 'Absences from the U.S.', name: 'absences' },
    { type: 'textarea', label: 'Travel Documents', name: 'travelDocuments' },
  
    // Part 5: Information About Your Family
    { type: 'text', label: 'Spouse\'s Information', name: 'spouseInfo', fields: ['Name', 'Date of Birth', 'A-Number'] },
    { type: 'text', label: 'Children\'s Information', name: 'childrenInfo', fields: ['Name', 'Date of Birth', 'A-Number'] },
  
    // Part 6: Additional Information
    { type: 'textarea', label: 'Other Names Used', name: 'additionalNames' },
    { type: 'textarea', label: 'U.S. Addresses Used', name: 'usAddresses' },
    { type: 'textarea', label: 'Current or Last Employer', name: 'employer' },
  
    // Part 7: Applicant's Statement, Contact Information, Declaration, Certification, and Signature
    { type: 'checkbox', label: 'Applicant\'s Statement', name: 'applicantStatement', options: ['I can read and understand English', 'The interpreter named in Part 8 read to me'] },
    { type: 'text', label: 'Applicant\'s Contact Information', name: 'applicantContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Applicant\'s Declaration and Certification', name: 'applicantDeclaration' },
    { type: 'signature', label: 'Applicant\'s Signature', name: 'applicantSignature' },
    { type: 'date', label: 'Date of Signature', name: 'signatureDate' },
  
    // Part 8: Interpreter's Contact Information, Certification, and Signature
    { type: 'text', label: 'Interpreter\'s Full Name', name: 'interpreterName' },
    { type: 'text', label: 'Interpreter\'s Business or Organization Name', name: 'interpreterBusiness' },
    { type: 'address', label: 'Interpreter\'s Mailing Address', name: 'interpreterAddress' },
    { type: 'text', label: 'Interpreter\'s Contact Information', name: 'interpreterContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Interpreter\'s Certification', name: 'interpreterCertification' },
    { type: 'signature', label: 'Interpreter\'s Signature', name: 'interpreterSignature' },
    { type: 'date', label: 'Date of Signature', name: 'interpreterSignatureDate' },
  
    // Part 9: Preparer's Contact Information, Declaration, and Signature
    { type: 'text', label: 'Preparer\'s Full Name', name: 'preparerName' },
    { type: 'text', label: 'Preparer\'s Business or Organization Name', name: 'preparerBusiness' },
    { type: 'address', label: 'Preparer\'s Mailing Address', name: 'preparerAddress' },
    { type: 'text', label: 'Preparer\'s Contact Information', name: 'preparerContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Preparer\'s Statement', name: 'preparerStatement' },
    { type: 'textarea', label: 'Preparer\'s Declaration', name: 'preparerDeclaration' },
    { type: 'signature', label: 'Preparer\'s Signature', name: 'preparerSignature' },
    { type: 'date', label: 'Date of Signature', name: 'preparerSignatureDate' },
  
    // Part 10: Additional Information
    { type: 'textarea', label: 'Additional Information', name: 'additionalInfo', fields: ['Page Number', 'Part Number', 'Item Number', 'Additional Information'] }
  ];

  const formI912 = [
    // Part 1: Basis for Your Request
    { type: 'radio', label: 'Basis for Your Request', name: 'basisForRequest', options: ['Means-tested benefit', 'Income at or below 150% of the Federal Poverty Guidelines', 'Financial hardship'] },
  
    // Part 2: Your Information
    { type: 'text', label: 'Full Name', name: 'fullName', fields: ['First name', 'Middle name', 'Last name'] },
    { type: 'text', label: 'Other Names Used', name: 'otherNamesUsed', fields: ['First name', 'Middle name', 'Last name'] },
    { type: 'address', label: 'U.S. Mailing Address', name: 'usMailingAddress' },
    { type: 'address', label: 'U.S. Physical Address', name: 'usPhysicalAddress' },
    { type: 'date', label: 'Date of Birth', name: 'dateOfBirth' },
    { type: 'text', label: 'Alien Registration Number (A-Number)', name: 'aNumber' },
    { type: 'text', label: 'USCIS Online Account Number', name: 'uscisOnlineAccountNumber' },
    { type: 'text', label: 'Marital Status', name: 'maritalStatus' },
    { type: 'number', label: 'Household Size and Income', name: 'householdSizeIncome' },
  
    // Part 3: Household Member's Information
    { type: 'text', label: 'Household Member\'s Full Name', name: 'householdMemberName', fields: ['First name', 'Middle name', 'Last name'] },
    { type: 'text', label: 'Relationship to You', name: 'relationship' },
    { type: 'number', label: 'Household Member\'s Income', name: 'householdMemberIncome' },
    { type: 'number', label: 'Household Member\'s Contribution to Household Income', name: 'householdMemberContribution' },
  
    // Part 4: Means-Tested Benefit
    { type: 'text', label: 'Benefit Granting Agency', name: 'benefitAgency' },
    { type: 'text', label: 'Type of Benefit Received', name: 'benefitType' },
    { type: 'date', label: 'Benefit Granted Date', name: 'benefitGrantedDate' },
  
    // Part 5: Income at or Below 150% of the Federal Poverty Guidelines
    { type: 'number', label: 'Household Size', name: 'householdSize' },
    { type: 'number', label: 'Total Household Income', name: 'householdIncome' },
    { type: 'textarea', label: 'Income Sources', name: 'incomeSources' },
  
    // Part 6: Financial Hardship
    { type: 'textarea', label: 'Describe Your Financial Hardship', name: 'financialHardship' },
  
    // Part 7: Applicant's Statement, Contact Information, Declaration, Certification, and Signature
    { type: 'checkbox', label: 'Applicant\'s Statement', name: 'applicantStatement', options: ['I can read and understand English', 'The interpreter named in Part 8 read to me'] },
    { type: 'text', label: 'Applicant\'s Contact Information', name: 'applicantContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Applicant\'s Declaration and Certification', name: 'applicantDeclaration' },
    { type: 'signature', label: 'Applicant\'s Signature', name: 'applicantSignature' },
    { type: 'date', label: 'Date of Signature', name: 'signatureDate' },
  
    // Part 8: Interpreter's Contact Information, Certification, and Signature
    { type: 'text', label: 'Interpreter\'s Full Name', name: 'interpreterName' },
    { type: 'text', label: 'Interpreter\'s Business or Organization Name', name: 'interpreterBusiness' },
    { type: 'address', label: 'Interpreter\'s Mailing Address', name: 'interpreterAddress' },
    { type: 'text', label: 'Interpreter\'s Contact Information', name: 'interpreterContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Interpreter\'s Certification', name: 'interpreterCertification' },
    { type: 'signature', label: 'Interpreter\'s Signature', name: 'interpreterSignature' },
    { type: 'date', label: 'Date of Signature', name: 'interpreterSignatureDate' },
  
    // Part 9: Preparer's Contact Information, Declaration, and Signature
    { type: 'text', label: 'Preparer\'s Full Name', name: 'preparerName' },
    { type: 'text', label: 'Preparer\'s Business or Organization Name', name: 'preparerBusiness' },
    { type: 'address', label: 'Preparer\'s Mailing Address', name: 'preparerAddress' },
    { type: 'text', label: 'Preparer\'s Contact Information', name: 'preparerContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Preparer\'s Statement', name: 'preparerStatement' },
    { type: 'textarea', label: 'Preparer\'s Declaration', name: 'preparerDeclaration' },
    { type: 'signature', label: 'Preparer\'s Signature', name: 'preparerSignature' },
    { type: 'date', label: 'Date of Signature', name: 'preparerSignatureDate' }
  ];
  const formI765 = [
    // Part 1: Reason for Applying
    { type: 'radio', label: 'Reason for Applying', name: 'reasonForApplying', options: ['Initial permission to accept employment', 'Replacement of lost or damaged EAD', 'Renewal of permission to accept employment'] },
  
    // Part 2: Information About You
    { type: 'text', label: 'Full Name', name: 'fullName', fields: ['First name', 'Middle name', 'Last name'] },
    { type: 'text', label: 'Other Names Used', name: 'otherNamesUsed', fields: ['First name', 'Middle name', 'Last name'] },
    { type: 'address', label: 'U.S. Mailing Address', name: 'usMailingAddress' },
    { type: 'address', label: 'U.S. Physical Address', name: 'usPhysicalAddress' },
    { type: 'text', label: 'Country of Citizenship or Nationality', name: 'countryOfCitizenship' },
    { type: 'text', label: 'Place of Birth', name: 'placeOfBirth', fields: ['City or Town', 'State or Province', 'Country'] },
    { type: 'date', label: 'Date of Birth', name: 'dateOfBirth' },
    { type: 'radio', label: 'Gender', name: 'gender', options: ['Male', 'Female'] },
    { type: 'radio', label: 'Marital Status', name: 'maritalStatus', options: ['Single', 'Married', 'Divorced', 'Widowed'] },
    { type: 'text', label: 'Social Security Number', name: 'ssn' },
    { type: 'text', label: 'Alien Registration Number (A-Number)', name: 'aNumber' },
    { type: 'text', label: 'USCIS Online Account Number', name: 'uscisOnlineAccountNumber' },
    { type: 'date', label: 'Date of Last Entry into the U.S.', name: 'lastEntryDate' },
    { type: 'text', label: 'Place of Last Entry into the U.S.', name: 'lastEntryPlace', fields: ['City or Town', 'State'] },
    { type: 'text', label: 'Immigration Status at Last Entry', name: 'statusAtLastEntry' },
    { type: 'text', label: 'Current Immigration Status', name: 'currentStatus' },
    { type: 'date', label: 'Current Status Expiration Date', name: 'statusExpirationDate' },
  
    // Part 3: Applicant's Statement, Contact Information, Declaration, Certification, and Signature
    { type: 'checkbox', label: 'Applicant\'s Statement', name: 'applicantStatement', options: ['I can read and understand English', 'The interpreter named in Part 4 read to me'] },
    { type: 'text', label: 'Applicant\'s Contact Information', name: 'applicantContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Applicant\'s Declaration and Certification', name: 'applicantDeclaration' },
    { type: 'signature', label: 'Applicant\'s Signature', name: 'applicantSignature' },
    { type: 'date', label: 'Date of Signature', name: 'signatureDate' },
  
    // Part 4: Interpreter's Contact Information, Certification, and Signature
    { type: 'text', label: 'Interpreter\'s Full Name', name: 'interpreterName' },
    { type: 'text', label: 'Interpreter\'s Business or Organization Name', name: 'interpreterBusiness' },
    { type: 'address', label: 'Interpreter\'s Mailing Address', name: 'interpreterAddress' },
    { type: 'text', label: 'Interpreter\'s Contact Information', name: 'interpreterContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Interpreter\'s Certification', name: 'interpreterCertification' },
    { type: 'signature', label: 'Interpreter\'s Signature', name: 'interpreterSignature' },
    { type: 'date', label: 'Date of Signature', name: 'interpreterSignatureDate' },
  
    // Part 5: Preparer's Contact Information, Declaration, and Signature
    { type: 'text', label: 'Preparer\'s Full Name', name: 'preparerName' },
    { type: 'text', label: 'Preparer\'s Business or Organization Name', name: 'preparerBusiness' },
    { type: 'address', label: 'Preparer\'s Mailing Address', name: 'preparerAddress' },
    { type: 'text', label: 'Preparer\'s Contact Information', name: 'preparerContact', fields: ['Daytime Telephone Number', 'Mobile Telephone Number', 'Email Address'] },
    { type: 'textarea', label: 'Preparer\'s Statement', name: 'preparerStatement' },
    { type: 'textarea', label: 'Preparer\'s Declaration', name: 'preparerDeclaration' },
    { type: 'signature', label: 'Preparer\'s Signature', name: 'preparerSignature' },
    { type: 'date', label: 'Date of Signature', name: 'preparerSignatureDate' },
  
    // Part 6: Additional Information
    { type: 'textarea', label: 'Additional Information', name: 'additionalInfo', fields: ['Page Number', 'Part Number', 'Item Number', 'Additional Information'] }
  ];
    
