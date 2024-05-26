import PyPDF2
import PyPDF2.generic
import os
from PyPDF2.errors import DependencyError
from pdf2image import convert_from_path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

pdf_path = 'i-821.pdf'
output_pdf = 'i-821_filled.pdf'
output_folder = './'
field_values = {

    # Barcode and Identification
    'PDF417BarCode1[0]': '123456789',

    # General Information
    'G28CheckBox[0]': 'Yes',
    'BarNumber_Txt[0]': 'A123456789',
    'USCISNumber_Txt[0]': '987654321',

    # Application Type
    'Part1_Item1_ApplicationType[0]': 'Type1',
    'Part1_Item1_ApplicationType[1]': 'Type2',
    'Part1_Item2_GrantedTPSU[0]': 'Yes',
    'Part1_Item2_GrantedTPSI[0]': 'No',
    'Part1_Item3_EADApp[0]': 'Yes',
    'Part1_Item3_EADApp[1]': 'No',
    'Part1_TPScountry[0]': 'CountryName',

    # Personal Information
    'Part2_Item1_FamilyName[0]': 'Doe',
    'Part2_Item1_GivenName[0]': 'John',
    'Part2_Item1_MiddleName[0]': 'M',
    'Part2_Item3_FamilyName[0]': 'Doe',
    'Part2_Item3_GivenName[0]': 'John',
    'Part2_Item3_MiddleName[0]': 'M',
    'Part2_Item2_FamilyName[0]': 'Doe',
    'Part2_Item2_GivenName[0]': 'Jane',
    'Part2_Item2_MiddleName[0]': 'A',
    'Part2_Item4_InCareofName[0]': 'Guardian Name',
    'Part2_Item4_StreetNumberName[0]': '123 Main St',
    'Part2_Item4_Unit[0]': 'Apt',
    'Part2_Item4_Unit[1]': 'Unit 1',
    'Part2_Item4_Unit[2]': 'Unit 2',
    'Part2_Item4_AptSteFlrNumber[0]': '1',
    'Part2_Item4_CityOrTown[0]': 'Anytown',
    'Part2_Item4_State[0]': 'NY',
    'Part2_Item4_ZipCode[0]': '12345',
    'Part2_Item5_YN[0]': 'Yes',
    'Part2_Item5_YN[1]': 'No',
    'Part2_Item6_StreetNumberName[0]': '456 Another St',
    'Part2_Item6_Unit[0]': 'Suite',
    'Part2_Item6_Unit[1]': 'Unit 1',
    'Part2_Item6_Unit[2]': 'Unit 2',
    'Part2_Item6_AptSteFlrNumber[0]': '2',
    'Part2_Item6_CityOrTown[0]': 'Othertown',
    'Part2_Item6_State[0]': 'CA',
    'Part2_Item6_ZipCode[0]': '67890',
    'Part2_Item8_AcctIdentifier[0]': 'ABC123',
    'Part2_Item10_DateOfBirth[0]': '01/01/1990',
    'Part2_Item11_DateOfBirth[0]': '01/01/1990',
    'Part2_Item11_DateOfBirth[1]': '01/02/1990',
    'Part2_Item12_Gender[0]': 'Male',
    'Part2_Item12_Gender[1]': 'Female',
    'Part2_Item13_CityOrTown[0]': 'Birth City',
    'Part2_Item14_CountryofBirth[0]': 'Birth Country',
    'Part2_Item17_MaritalStatus[0]': 'Single',
    'Part2_Item17_MaritalStatus[1]': 'Married',
    'Part2_Item17_MaritalStatus[2]': 'Divorced',
    'Part2_Item17_MaritalStatus[3]': 'Widowed',
    'Part2_Item17_MaritalStatus[4]': 'Separated',
    'Part2_Item17_MaritalStatus[5]': 'Other',
    'Part2_Item17_MaritalStatus[6]': 'Unknown',
    'Part2_Item17_MaritalStatusOther[0]': 'Other Status',
    'Part2_Item7_AlienNumber[0]': 'A123456789',
    'Part2_Item9_SocialSecurityNumber[0]': '123-45-6789',
    'Part2_Item15a[0]': 'Other Info 1',
    'Part2_Item15b[0]': 'Other Info 2',
    'Part2_Item15c[0]': 'Other Info 3',
    'Part2_Item15d[0]': 'Other Info 4',
    'Part2_Item16a[0]': 'Other Info 5',
    'Part2_Item16b[0]': 'Other Info 6',
    'Part2_Item16c[0]': 'Other Info 7',
    'Part2_Item16d[0]': 'Other Info 8',
    'Part2_Item22_Passport[0]': 'Passport Number',
    'Part2_Item22_Passport[1]': 'Second Passport Number',
    'Part2_Item31e_Present[0]': 'Present',
    'Part2_Item22_I94[0]': 'I94 Number',

    # Immigration Status
    'P2_Line7_DateOfBirth[0]': "12/12/2024",
    'Part2_Item19_ImmigrationStatus[0]': 'Status 1',
    'Part2_Item20_PortofEntry[0]': 'Port',
    'Part2_Item20_CityOrTown[0]': 'Entry City',
    'Part2_Item20_State[0]': 'Entry State',
    'Part2_Item21_AuthorizedPdofStay[0]': 'Authorized Period',
    'Part2_Item23a_AddlPassport[0]': 'Additional Passport 1',
    'Part2_Item23b_AddlPassport[0]': 'Additional Passport 2',
    'Part2_Item24_CountryofIssuance[0]': 'Country of Issuance',
    'Part2_Item24_PassportExpiration[0]': 'Passport Expiration',
    'Part2_Item25_ImmigrationStatus[0]': 'Current Status',
    'Part2_Item25_ImmigrationProceedings[0]': 'Yes',
    'Part2_Item25_ImmigrationProceedings[1]': 'No',
    'Part2_Item27_ProceedingType[0]': 'Type 1',
    'Part2_Item27_ProceedingType[1]': 'Type 2',
    'Part2_Item27_ProceedingType[2]': 'Type 3',
    'Part2_Item28_LocDOJProceedings[0]': 'Location DOJ',
    'Part2_Item29_LocFedCtProceedings[0]': 'Location Federal Court',
    'Part2_Item31a_ProceedingDateFrom[0]': 'Date From',
    'Part2_Item31b_ProceedingDateTo[0]': 'Date To',

    # Ethnicity and Race
    'Part3_Item1_Ethnicity[0]': 'Hispanic or Latino',
    'Part3_Item1_Ethnicity[1]': 'Not Hispanic or Latino',
    'Part3_Item2_RaceW[0]': 'White',
    'Part3_Item2_RaceA[0]': 'Asian',
    'Part3_Item2_RaceB[0]': 'Black or African American',
    'Part3_Item2_RaceI[0]': 'American Indian or Alaska Native',
    'Part3_Item2_RaceH[0]': 'Native Hawaiian or Other Pacific Islander',

    # Eye and Hair Color
    'Part3_Item5_Eyecolor[0]': 'Black',
    'Part3_Item5_Eyecolor[1]': 'Blue',
    'Part3_Item5_Eyecolor[2]': 'Brown',
    'Part3_Item5_Eyecolor[3]': 'Gray',
    'Part3_Item5_Eyecolor[4]': 'Green',
    'Part3_Item5_Eyecolor[5]': 'Hazel',
    'Part3_Item5_Eyecolor[6]': 'Maroon',
    'Part3_Item5_Eyecolor[7]': 'Pink',
    'Part3_Item5_Eyecolor[8]': 'Unknown/Other',

    'Part3_Item6_Haircolor[0]': 'Bald',
    'Part3_Item6_Haircolor[1]': 'Black',
    'Part3_Item6_Haircolor[2]': 'Blonde',
    'Part3_Item6_Haircolor[3]': 'Brown',
    'Part3_Item6_Haircolor[4]': 'Gray',
    'Part3_Item6_Haircolor[5]': 'Red',
    'Part3_Item6_Haircolor[6]': 'Sandy',
    'Part3_Item6_Haircolor[7]': 'White',
    'Part3_Item6_Haircolor[8]': 'Unknown/Other',

    # Height
    'Pt2Line3_HeightFeet[0]': '5',
    'Pt2Line3_HeightInches[0]': '11',
    'Pt2Line4_HeightInches2[0]': '11',
    'Pt2Line4_HeightInches1[0]': '11',
    'Pt2Line4_HeightInches3[0]': '11',

    # Addresses and Contact Information
    'Part4_Item1_USCISNumber[0]': 'A123456789',
    'Part4_Item3_FamilyName[0]': 'Doe',
    'Part4_Item3_GivenName[0]': 'John',
    'Part4_Item3_MiddleName[0]': 'M',
    'Part4_Item4_StreetNumberName[0]': '123 Main St',
    'Part4_Item4_Unit[0]': 'Apt',
    'Part4_Item4_Unit[1]': 'Unit 1',
    'Part4_Item4_Unit[2]': 'Unit 2',
    'Part4_Item4_AptSteFlrNumber[0]': '1',
    'Part4_Item4_CityOrTown[0]': 'Anytown',
    'Part4_Item4_State[0]': 'NY',
    'Part4_Item4_ZipCode[0]': '12345',
    'Part4_Item4_Province[0]': 'Province',
    'Part4_Item4_PostalCode[0]': 'Postal Code',
    'Part4_Item4_Country[0]': 'Country',
    'Part4_Item5_DateOfBirth[0]': '01/01/1990',
    'Part4_Item6_DateOfMarriage[0]': '01/01/2010',
    'Part4_Item7_PlaceofMarriage[0]': 'Place of Marriage',
    'Part4_Item8_CityOrTown[0]': 'City',
    'Part4_Item8_Province[0]': 'Province',
    'Part4_Item8_Country[0]': 'Country',
    'Part4_Item9_TPSY[0]': 'Yes',
    'Part4_Item9_TPSN[0]': 'No',
    'Part4_Item10b_DateFrom[0]': '01/01/2000',
    'Part4_Item10c_DateTo[0]': '01/01/2010',
    'Part4_Item10d_Present[0]': 'Present',
    'Part4_Item10e_IDK[0]': 'I don\'t know',
    'Part4_Item2_AlienNumber[0]': 'A123456789',
    'Part4_Item8_State[0]': 'State',

    # Alien Numbers
    'Part5_Item3_AlienNumber[0]': 'A123456789',
    'Part5_Item13_AlienNumber[0]': 'A987654321',
    'Part6_Item3_AlienNumber[0]': 'A567890123',
    'Part6_Item10_AlienNumber[0]': 'A098765432',

    # Spouse Information
    'Part5_Item1_FamilyName[0]': 'Doe',
    'Part5_Item1_GivenName[0]': 'Jane',
    'Part5_Item1_MiddleName[0]': 'A',
    'Part5_Item2_FSpouseNationalities[0]': 'Nationality',
    'Part5_Item4_FSpouseDOB[0]': '02/02/1992',
    'Part5_Item5_FSpouseDOD[0]': '02/02/2022',
    'Part5_Item6_MarriageFrom[0]': '02/02/2010',
    'Part5_Item6_MarriageTo[0]': '02/02/2020',
    'Part5_Item7_MarriageEnded[0]': 'Yes',
    'Part5_Item8_YDI[0]': 'Yes',
    'Part5_Item8_YDI[1]': 'No',
    'Part5_Item8_YDI[2]': 'Don\'t know',
    'Part5_Item9a_DateFrom[0]': '01/01/2000',
    'Part5_Item9b_DateTo[0]': '01/01/2010',
    'Part5_Item9c_Present[0]': 'Present',
    'Part5_Item9d_IDK[0]': 'I don\'t know',
    'Part5_Item10_YNI[0]': 'Yes',
    'Part5_Item10_YNI[1]': 'No',
    'Part5_Item10_YNI[2]': 'I don\'t know',
    'Part5_Item11_FamilyName[0]': 'Doe',
    'Part5_Item11_GivenName[0]': 'John Jr.',
    'Part5_Item11_MiddleName[0]': 'B',
    'Part5_Item12_FSpouseNationalities[0]': 'Nationality',
    'Part5_Item14_FSpouseDOB[0]': '03/03/1993',
    'Part5_Item15_FSpouseDOD[0]': '03/03/2023',
    'Part5_Item16_MarriageFrom[0]': '03/03/2011',
    'Part5_Item16_MarriageTo[0]': '03/03/2021',
    'Part5_Item17_MarriageEnded[0]': 'Yes',
    'Part5_Item18_YNI[0]': 'Yes',
    'Part5_Item18_YNI[1]': 'No',
    'Part5_Item18_YNI[2]': 'I don\'t know',
    'Part5_Item19a_DateFrom[0]': '01/01/2001',
    'Part5_Item19b_DateTo[0]': '01/01/2011',
    'Part5_Item19c_Present[0]': 'Present',
    'Part5_Item19d_IDK[0]': 'I don\'t know',
    'Part5_Item20_YNI[0]': 'Yes',
    'Part5_Item20_YNI[1]': 'No',
    'Part5_Item20_YNI[2]': 'I don\'t know',

    # Child Information
    'Part6_Item1_FamilyName[0]': 'Doe',
    'Part6_Item1_GivenName[0]': 'Junior',
    'Part6_Item1_MiddleName[0]': 'J',
    'Part6_Item2_USCISNumber[0]': 'A123456789',
    'Part6_Item4_DateOfBirth[0]': '04/04/2004',
    'Part6_Item5_StreetNumberName[0]': '789 New St',
    'Part6_Item5_Unit[0]': 'Unit',
    'Part6_Item5_Unit[1]': 'Unit 1',
    'Part6_Item5_Unit[2]': 'Unit 2',
    'Part6_Item5_AptSteFlrNumber[0]': '3',
    'Part6_Item5_CityOrTown[0]': 'Sometown',
    'Part6_Item5_State[0]': 'TX',
    'Part6_Item5_ZipCode[0]': '45678',
    'Part6_Item5_Province[0]': 'Province',
    'Part6_Item5_PostalCode[0]': 'Postal Code',
    'Part6_Item5_Country[0]': 'Country',
    'Part6_Item6_ChildTPSFrom[0]': 'Yes',
    'Part6_Item6_ChildTPSTo[0]': 'No',
    'Part6_Item8_FamilyName[0]': 'Doe',
    'Part6_Item8_GivenName[0]': 'Junior Jr.',
    'Part6_Item8_MiddleName[0]': 'JJ',
    'Part6_Item11_DateOfBirth[0]': '04/04/2004',
    'Part6_Item12_StreetNumberName[0]': '789 New St',
    'Part6_Item12_Unit[0]': 'Unit',
    'Part6_Item12_Unit[1]': 'Unit 1',
    'Part6_Item12_Unit[2]': 'Unit 2',
    'Part6_Item12_AptSteFlrNumber[0]': '3',
    'Part6_Item12_CityOrTown[0]': 'Sometown',
    'Part6_Item12_State[0]': 'TX',
    'Part6_Item12_ZipCode[0]': '45678',
    'Part6_Item12_Province[0]': 'Province',
    'Part6_Item12_PostalCode[0]': 'Postal Code',
    'Part6_Item12_Country[0]': 'Country',
    'Part6_Item13_ChildTPSFrom[0]': 'Yes',
    'Part6_Item12_ChildTPSTo[0]': 'No',
    'Part6_Item14_ChildAppTPS[0]': 'Yes',
    'Part6_Item14_ChildAppTPS[1]': 'No',

    # Country of Residence
    'Part7_Item1_CountryResidence[0]': 'Country',

    # Travel Information
    'Part7_Item1_EnterUS[0]': 'Yes',
    'Part7_Item1_Travel[0]': 'Yes',
    'Part7_Item1_Travel[1]': 'No',
    'Part7_Item2_CountriesTraveled[0]': 'Country 1',
    'Part7_Item2_CountriesTraveledFrom[0]': 'Country 2',
    'Part7_Item2_CountriesTraveledTo[0]': 'Country 3',
    'Part7_Item2_ImmigrationStatus[0]': 'Status',
    'Part7_Item2_ImmigrationOffer[0]': 'Yes',
    'Part7_Item2_ImmigrationOffer[1]': 'No',
    'Part7_Item2_DescribeCountries[0]': 'Description',
    'Part7_Item2_DidNotAccept[0]': 'Yes',
    'Part7_Item4a_YN[0]': 'Yes',
    'Part7_Item4a_YN[1]': 'No',
    'Part7_Item4b_YN[0]': 'Yes',
    'Part7_Item4b_YN[1]': 'No',

    # Yes/No Questions
    'Part7_Item4c_YN[0]': 'Yes',
    'Part7_Item4c_YN[1]': 'No',
    'Part7_Item5a_YN[0]': 'Yes',
    'Part7_Item5a_YN[1]': 'No',
    'Part7_Item5b_YN[0]': 'Yes',
    'Part7_Item5b_YN[1]': 'No',
    'Part7_Item5c_YN[0]': 'Yes',
    'Part7_Item5c_YN[1]': 'No',
    'Part7_Item7a_YN[0]': 'Yes',
    'Part7_Item7a_YN[1]': 'No',
    'Part7_Item7b_YN[0]': 'Yes',
    'Part7_Item7b_YN[1]': 'No',
    'Part7_Item7c_YN[0]': 'Yes',
    'Part7_Item7c_YN[1]': 'No',
    'Part7_Item8_YN[0]': 'Yes',
    'Part7_Item8_YN[1]': 'No',
    'Part7_Item9a_YN[0]': 'Yes',
    'Part7_Item9a_YN[1]': 'No',
    'Part7_Item9b_YN[0]': 'Yes',
    'Part7_Item9b_YN[1]': 'No',
    'Part7_Item9c_YN[0]': 'Yes',
    'Part7_Item9c_YN[1]': 'No',
    'Part7_Item9d_YN[0]': 'Yes',
    'Part7_Item9d_YN[1]': 'No',
    'Part7_Item9e_YN[0]': 'Yes',
    'Part7_Item9e_YN[1]': 'No',
    'Part7_Item11a_YN[0]': 'Yes',
    'Part7_Item11a_YN[1]': 'No',
    'Part7_Item11b_YN[0]': 'Yes',
    'Part7_Item11b_YN[1]': 'No',
    'Part7_Item11c_YN[0]': 'Yes',
    'Part7_Item11c_YN[1]': 'No',
    'Part7_Item11d_YN[0]': 'Yes',
    'Part7_Item11d_YN[1]': 'No',
    'Part7_Item12a_YN[0]': 'Yes',
    'Part7_Item12a_YN[1]': 'No',
    'Part7_Item12b_YN[0]': 'Yes',
    'Part7_Item12b_YN[1]': 'No',
    'Part7_Item12c_YN[0]': 'Yes',
    'Part7_Item12c_YN[1]': 'No',
    'Part7_Item12d_YN[0]': 'Yes',
    'Part7_Item12d_YN[1]': 'No',
    'Part7_Item13a_YN[0]': 'Yes',
    'Part7_Item13a_YN[1]': 'No',
    'Part7_Item13b_YN[0]': 'Yes',
    'Part7_Item13b_YN[1]': 'No',
    'Part7_Item13c_YN[0]': 'Yes',
    'Part7_Item13c_YN[1]': 'No',
    'Part7_Item17_YN[0]': 'Yes',
    'Part7_Item17_YN[1]': 'No',
    'Part7_Item18a_YN[0]': 'Yes',
    'Part7_Item18a_YN[1]': 'No',
    'Part7_Item18b_YN[0]': 'Yes',
    'Part7_Item18b_YN[1]': 'No',
    'Part7_Item18c_YN[0]': 'Yes',
    'Part7_Item18c_YN[1]': 'No',
    'Part7_Item18d_YND[0]': 'Yes',
    'Part7_Item18d_YND[1]': 'No',
    'Part7_Item18e_YND[0]': 'Yes',
    'Part7_Item18e_YND[1]': 'No',
    'Part7_Item18d_YND[2]': 'Don\'t know',
    'Part7_Item19_YND[0]': 'Yes',
    'Part7_Item19_YND[1]': 'No',
    'Part7_Item20_YND[0]': 'Yes',
    'Part7_Item20_YND[1]': 'No',
    'Part7_Item21a_YND[0]': 'Yes',
    'Part7_Item21a_YND[1]': 'No',
    'Part7_Item21b_YND[0]': 'Yes',
    'Part7_Item21b_YND[1]': 'No',
    'Part7_Item21c_YND[0]': 'Yes',
    'Part7_Item21c_YND[1]': 'No',
    'Part7_Item22_YND[0]': 'Yes',
    'Part7_Item22_YND[1]': 'No',
    'Part7_Item23_YND[0]': 'Yes',
    'Part7_Item23_YND[1]': 'No',
    'Part7_Item24_YND[0]': 'Yes',
    'Part7_Item24_YND[1]': 'No',
    'Part7_Item25_YND[0]': 'Yes',
    'Part7_Item25_YND[1]': 'No',
    'Part7_Item26_YND[0]': 'Yes',
    'Part7_Item26_YND[1]': 'No',
    'Part7_Item16c_YN[0]': 'Yes',
    'Part7_Item16c_YN[1]': 'No',
    'Part7_Item16b_YN[0]': 'Yes',
    'Part7_Item16b_YN[1]': 'No',
    'Part7_Item27_YND[0]': 'Yes',
    'Part7_Item27_YND[1]': 'No',
    'Part7_Item29a_YN[0]': 'Yes',
    'Part7_Item29a_YN[1]': 'No',
    'Part7_Item29b_YN[0]': 'Yes',
    'Part7_Item29b_YN[1]': 'No',
    'Part7_Item29c_YN[0]': 'Yes',
    'Part7_Item29c_YN[1]': 'No',
    'Part7_Item29d_YN[0]': 'Yes',
    'Part7_Item29d_YN[1]': 'No',
    'Part7_Item29e_YN[0]': 'Yes',
    'Part7_Item29e_YN[1]': 'No',
    'Part7_Item14_YN[0]': 'Yes',
    'Part7_Item14_YN[1]': 'No',
    'Part7_Item15_YN[0]': 'Yes',
    'Part7_Item15_YN[1]': 'No',
    'Part7_Item16a_YN[0]': 'Yes',
    'Part7_Item16a_YN[1]': 'No',
    'Part7_Item33_YN[0]': 'Yes',
    'Part7_Item33_YN[1]': 'No',
    'Part7_Item34_YN[0]': 'Yes',
    'Part7_Item34_YN[1]': 'No',
    'Part7_Item35_YN[0]': 'Yes',
    'Part7_Item35_YN[1]': 'No',
    'Part7_Item36_YN[0]': 'Yes',
    'Part7_Item36_YN[1]': 'No',
    'Part7_Item37a_YN[0]': 'Yes',
    'Part7_Item37a_YN[1]': 'No',
    'Part7_Item37b_YN[0]': 'Yes',
    'Part7_Item37b_YN[1]': 'No',
    'Part7_Item38a_YN[0]': 'Yes',
    'Part7_Item38a_YN[1]': 'No',
    'Part7_Item38b_YN[0]': 'Yes',
    'Part7_Item38b_YN[1]': 'No',
    'Part7_Item38c_YN[0]': 'Yes',
    'Part7_Item38c_YN[1]': 'No',
    'Part7_Item38d_YN[0]': 'Yes',
    'Part7_Item38d_YN[1]': 'No',
    'Part7_Item38e_YN[0]': 'Yes',
    'Part7_Item38e_YN[1]': 'No',
    'Part7_Item39a_YN[0]': 'Yes',
    'Part7_Item39a_YN[1]': 'No',
    'Part7_Item39b_YN[0]': 'Yes',
    'Part7_Item39b_YN[1]': 'No',
    'Part7_Item40a_YN[0]': 'Yes',
    'Part7_Item40a_YN[1]': 'No',
    'Part7_Item41_YN[0]': 'Yes',
    'Part7_Item41_YN[1]': 'No',
    'Part8_Item1_AppStmt[0]': 'Statement',
    'Part8_Item2_Preparer[0]': 'Preparer',
    'Part8_Item2_PrepName[0]': 'Preparer Name',
    'Part8_Item1_AppStmt[1]': 'Statement',
    'Part8_Item1_Language[0]': 'Language',
    'Part7_Item31a_YN[0]': 'Yes',
    'Part7_Item31a_YN[1]': 'No',
    'Part7_Item31b_YN[0]': 'Yes',
    'Part7_Item31b_YN[1]': 'No',
    'Part7_Item32_YN[0]': 'Yes',
    'Part7_Item32_YN[1]': 'No',

    # Preparer's Information
    'Part9_Item1_FamilyName[0]': 'Preparer Last Name',
    'Part9_Item1_GivenName[1]': 'Preparer First Name',
    'Part9_Item2_OrgName[0]': 'Organization Name',
    'Part9_Item3_StreetNumberName[0]': '123 Org St',
    'Part9_Item3_Unit[0]': 'Unit',
    'Part9_Item3_Unit[1]': 'Unit 1',
    'Part9_Item3_Unit[2]': 'Unit 2',
    'Part9_Item3_AptSteFlrNumber[0]': '5',
    'Part9_Item3_CityOrTown[0]': 'Org City',
    'Part9_Item3_State[0]': 'Org State',
    'Part9_Item3_ZipCode[0]': '45678',
    'Part9_Item3_Province[0]': 'Province',
    'Part9_Item3_PostalCode[0]': 'Postal Code',
    'Part9_Item3_Country[0]': 'Country',
    'Part8_Item6a_Signature[0]': 'Preparer Signature',
    'Part8_Item6b_DateofSignature[0]': '05/05/2024',
    'Part9_Item4_DaytimePhone[0]': '123-456-7890',
    'Part9_Item5_Email[0]': 'preparer@example.com',
    'Part10_Item5_MobilePhone[0]': '098-765-4321',
    'Part8_Item3_DayPhone[0]': '123-456-7890',
    'Part8_Item4_MobilePhone[0]': '098-765-4321',
    'Part8_Item5_Email[0]': 'applicant@example.com',
    'Part6_Item12_Province[0]': 'Province',

    # Signatures
    'Part9_Item6_Signature[0]': 'Applicant Signature',
    'Part9_Item6_DateofSignature[0]': '05/05/2024',
    'Part10_Item1_FamilyName[0]': 'Applicant Last Name',
    'Part10_Item1_GivenName[0]': 'Applicant First Name',
    'Part10_Item2_OrgName[0]': 'Organization Name',
    'Part10_Item3_StreetNumberName[0]': '123 Org St',
    'Part10_Item3_Unit[0]': 'Unit',
    'Part10_Item3_Unit[1]': 'Unit 1',
    'Part10_Item3_Unit[2]': 'Unit 2',
    'Part10_Item3_AptSteFlrNumber[0]': '5',
    'Part10_Item3_CityOrTown[0]': 'Org City',
    'Part10_Item3_State[0]': 'Org State',
    'Part10_Item3_ZipCode[0]': '45678',
    'Part10_Item3_Province[0]': 'Province',
    'Part10_Item3_PostalCode[0]': 'Postal Code',
    'Part10_Item3_Country[0]': 'Country',
    'Part10_Item7_PreparerStmt[0]': 'Statement',
    'Part10_Item7_PreparerStmt[1]': 'Statement',
    'Part10_Item7b_Extend[0]': 'Yes',
    'Part10_Item7b_NotExtend[0]': 'No',
    'Part10_Item8a_Signature[0]': 'Preparer Signature',
    'Part10_Item8b_DateofSignature[0]': '05/05/2024',
    'Part10_Item4_DaytimePhone[0]': '123-456-7890',
    'Part10_Item5_MobilePhone[0]': '098-765-4321',
    'Part10_Item6_Email[0]': 'preparer@example.com',
    'Part2_Item1_FamilyName[0]': 'Applicant Last Name',
    'Part2_Item1_GivenName[0]': 'Applicant First Name',
    'Part2_Item1_MiddleName[0]': 'Middle Name',
    'AI_3a_PageNumber[0]': '3',
    'AI_3b_PartNumber[0]': 'Part 3',
    'AI_3c_ItemNumber[0]': '1',
    'AI_3d_AdditionalInfo[0]': 'Additional Info',
    'AI_4a_PageNumber[0]': '4',
    'AI_4b_PartNumber[0]': 'Part 4',
    'AI_4c_ItemNumber[0]': '2',
    'AI_4d_AdditionalInfo[0]': 'Additional Info',
    'AI_5a_PageNumber[0]': '5',
    'AI_5b_PartNumber[0]': 'Part 5',
    'AI_5c_ItemNumber[0]': '3',
    'AI_6a_PageNumber[0]': '6',
    'AI_6b_PartNumber[0]': 'Part 6',
    'AI_6c_ItemNumber[0]': '4',
    'AI_7a_PageNumber[0]': '7',
    'AI_7b_PartNumber[0]': 'Part 7',
    'AI_7c_ItemNumber[0]': '5',
    'AI_7d_AdditionalInfo[0]': 'Additional Info',
    'AI_5d_AdditionalInfo[0]': 'Additional Info',
    'AI_6d_AdditionalInfo[0]': 'Additional Info'
}

def list_and_set_form_fields(pdf_path, output_path, field_values):

    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            writer = PyPDF2.PdfWriter()
            
            # Check if the PDF has any form fields
            if '/AcroForm' not in reader.trailer['/Root']:
                print("No form fields found in the PDF.")
                return
            
            form_fields = reader.get_form_text_fields()
            
            # Dictionary to store fields by page
            fields_by_page = {}
            
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                fields_by_page[page_num] = []
                
                if '/Annots' in page:
                    for annot in page['/Annots']:
                        field = annot.get_object()
                        if '/T' in field:
                            field_name = field['/T']
                            field_type = field['/FT']
                            fields_by_page[page_num].append(field_name)
                            # Set field value if it exists in the provided values
                            if field_name in field_values:
                                field.update({
                                    PyPDF2.generic.NameObject('/V'): PyPDF2.generic.create_string_object(field_values[field_name])
                                })
                            if field_type == '/Btn':
                                field.update({
                                    PyPDF2.generic.NameObject('/AS'): PyPDF2.generic.NameObject(next(iter(field['/AP']['/N'].keys())))
                                })
                
                writer.add_page(page)
            
            # Print the form fields page by page
            # for page_num, fields in fields_by_page.items():
                # print(f"Page {page_num + 1}:")
                # for field_name in fields:
                    # print(f" - {field_name}")
                # if not fields:
                    # print(" - No form fields on this page.")   
            
            # Save the modified PDF to a new file
            with open(output_path, 'wb') as output_pdf:
                writer.write(output_pdf)
    
    except DependencyError as e:
        print(f"Error: {e}. Please install PyCryptodome using 'pip install pycryptodome'.")

def pdf_to_jpg(pdf_path, output_folder):
    # Convert PDF to a list of PIL Image objects
    images = convert_from_path(pdf_path)
    
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Save each page as a JPG file
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f'page_{i + 1}.jpg')
        image.save(image_path, 'JPEG')

def natural_sort_key(s):
    """
    Key function for natural sorting.
    """
    import re
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def convert_images_to_pdf(folder_path, output_pdf):
    image_paths = [os.path.join(folder_path, f) for f in sorted(os.listdir(folder_path), key=natural_sort_key) if f.lower().endswith('.jpg')]
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    for image_path in image_paths:
        img = Image.open(image_path)
        img_width, img_height = img.size
        aspect_ratio = img_width / img_height
        if img_width > width or img_height > height:
            if aspect_ratio > 1:
                img_width = width
                img_height = width / aspect_ratio
            else:
                img_height = height
                img_width = height * aspect_ratio
        c.setPageSize((img_width, img_height))
        c.drawImage(image_path, 0, 0, img_width, img_height)
        c.showPage()
        img.close()  # Close the image file
        os.remove(image_path)  # Delete the JPG file
    c.save()

def code(pdf_path, output_pdf, output_folder, field_values):
    list_and_set_form_fields(pdf_path, output_pdf, field_values)
    pdf_to_jpg(output_pdf, output_folder)
    convert_images_to_pdf(output_folder, output_pdf)

code(pdf_path, output_pdf, output_folder, field_values)