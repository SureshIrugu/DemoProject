******************************************TEST STRATEGY******************************************

## Test Strategy for SauceDemo

TABLE OF CONTENTS
    - Overview
    - Test Strategy Overview
    - Test approach
    - Reporting and Metrics 
    - Risk and dependencies
    - Summary

 ## Overview
    This test strategy document for the Swag Labs web application, ensuring that it meets functional UI and API testing.

## Test Strategy Overview
    Objectives
        - To test that the agreed Business, Functional, and Operational user stories have been developed effectively and are being met by the solution.
        - Early identification of problems (defects) and changes, so that their resolution can be managed prior.
        - To ensure that implications of defects are identified and mitigated to enable an informed live decision and clarity on priorities.
        - Verify that all objects meet functional and technical specifications in the integrated environment.
        - Test realistic combinations of data and functionality based on identified business processes. 
        - Conduct tests on an environment.
        - Establish and use a common approach, process, and tools for all testing phases.  Re-use existing tools where possible.
        - Ensure roles testing during different environment.

    Testing Levels
        - Unit Testing: Takes place in the development environment before deploying into the test environment. 
             Ex: API, DB testing.
        - Functional Testing: Verify that all functionalities work as intended.
              - User Login/Logout
              - Product searaching and filtering in product listing page
              - Cart functionality (adding/removing items)
              - Checkout process
              - Error handling (invalid login, empty cart, etc.)
        - Regression Testing: to ensure that recent code changes do not introduce new defects or adversely affect existing functionalities.
        - Integration Testing: to verify that different components of the application interact correctly.
        - User Acceptance Testing: to validate that the application meets business requirements and is ready for deployment.

        Automation UI Testing: to ensure the UI behaves as expected across different scenarios and prevent regressions.
            - Tools: Playwright with Python.
            - Requirement focus:
            - User login/logout processes.
            - Product searaching and filtering in product listing page
            - Cart operations (adding/removing products).
            - Checkout flow.
            - Responsive design across various devices and screen sizes.
         Ensure: continues integration testing to run scripts
        
        API Testing:  to validate the functionality and performance of the backend APIs with valid and invalid cases.
            Tools: Playwright with Python, Postman.
            Environement: petcircle demo environment  uri - "https://petstore.swagger.io/"
            - Add new pet into the store
            - Upload pet image
            - Fetch pet id and details
            - Delete pet using id 
            - Store operations[inventory status, place order, find purchase order, etc.]
            - User opertations[create a user, Update user details, Login/Logout, delet user, ect..]
            
    Testing Environment 
        - Demo Environment: demo website "https://www.saucedemo.com/" for testing.
        - Browsers: Chrome
    
### Test approach
    -This project is use a Agile Methodology with scrum approach for Automation and manual testing. 
    Entry and Exit Criteria:
       Entry:
            Planning Readiness:
                - Test Strategy is complete.
                - Test Plan for the specific test phase is complete.
                - Test Management process and tools are setup and communicated.
                - Defect Management process are setup and communicated.
                - Reporting and related metrics have been developed.
            
            Resource readiness:
                - Test execution plan is prepared and aligned with test resources.
            
            Environment Readiness:
                - Test demo environment API, UI, DB available to shaken out.
                - Test data is in the environment / mechanism to generate test data is established.

            Execution Readiness:
                - Test scripts are in the test management tools,
                - Test scripts and execution plan are aligned with end to end.
                - Defect management sessions / communication channels are setup

       Exit criteria:
            Execution Completion:
                - Test scripts are 100% executed or have agreement to not be included in this test phase.
                - Test execution results are documented.
                - Open defects are resolved or have agreement / workaround to address.x
    
            Reporting Completion:
                - Test Closure Memo is complete.
                - Agreed test metrics for reporting are provided.
      
       Defect Management:
            Defect management is the process of capturing, triaging, fixing, and retesting defects throughout the test execution process. 
            The purpose of a consistent, structured defect lifecycle is to:
                - Provide clarity as to ownership and status of a defect.
                - Ensure all required actions are undertaken with severity and priority
                - Minimise the probability of the same issue appearing in later test phases.
            
            Defect Severity:
                Severity 1: The business impact of the defect is critical.
                            ex- Test environment is not functioning and testing cannot proceed i.e. Log-in failure.
                Severity 2: The entire application(s), components or business functionality will not work, but a business workaround is available.
                            ex: Vital user-interface is not working; however can perform function via native system interface.
                Severity 3: A minor part of the application(s) or business functionality does not work as expected.  The business functionality is nominally compromised.
                            ex: Help function does not work.
                Severity 4: The function does not perform as expected, however business functionality is not compromised.
                            ex: Cosmetic, navigational or similar issues exist.
            
            Defect Priority: Defect priority measure the impact on the overall test schedule of the defect remaining in the application.
                Priority 1: A problem where testing cannot continue.
                            ex: Vital user interface not working, and no access to native system.
                Priority 2: A problem where testing of a significant application component or function cannot continue.
                            ex: Vital user-interface not working; however can perform function via native system interface.
                 Priority 3: A problem that is not severe.
                             ex: Failures with minor and infrequently used functionality.
                Priority 4: A minor problem.
                             ex: Cosmetic, navigational, or similar issues exist
### Reporting and Metrics
    The status of test execution and defects identified will be reported to the relevant stakeholders with regualar basis.
        Reporting will focus on the following:
            - Automation Status Summary
            - Automation test Execution report
            - Defect Metrics e.g. Open defects by severity, Root cause of defects.
        Test reporting, the aim is to document and share to manager.
    
### Risk and dependencies 
    Risk 1: Overlapping functional test phase - environment. Eg.- environment is not available.
    Risk Mitigation 1: Delivery model will support test execution model.
    Risk 2: Hot fixes are not expected to impact overall project timelines.
    Risk Mitigation 2: Hotfixes, this will have to be assessed based on business criticality and impact.
### Summary
    This test strategy aims to provide a structured framework for validating the SauceDemo application.



******************************************TEST PLAN******************************************


### Table Contents
    1. Introduction
    2. Test Strategy
        - Objectives
        - Testing Levels
        - Test approach
            - Entry and Exit Criteria
        - Defect Management
    4. Resources
    5. Schedule
    6. Test Activities
    7. Test Risks and Mitigation Factors
    8. Environment
    9. Approval

### Introduction:
    This plan describes the testing approach overall framework that will drive the testing of the Swag Lab.
    The document introduce:
        - Test strategy
        - Execution strategy
        - Test management

### Test strategy
    Objectives
        The objective of the test is to verify that the functionality of Swag Lab demo works according to the specifications.
        The test will execute and verify the test scripts, identify, fix and retest all high and medium severity 
        defects per the entrance criteria, prioritize lower severity defects for future fixing.

    Testing Levels
        - Unit Testing
        - Functional Testing: Verify that all functionalities work as intended.
              - User Login/Logout
              - Product searaching and filtering in product listing page
              - Cart functionality (adding/removing items)
              - Checkout process
              - Error handling (invalid login, empty cart, etc.)
        - Regression Testing
        - Sanity Testing
        Automation UI Testing: to ensure the UI behaves as expected across different scenarios and prevent regressions.
            - Tools: Playwright with Python.
        API Testing:  to validate the functionality and performance of the backend APIs with valid and invalid cases.
            Tools: Playwright with Python, Postman.
            Environement: petcircle demo environment  uri - "https://petstore.swagger.io/".

    Testing Environment 
        - Demo Environment: demo website "https://www.saucedemo.com/" for testing.
        - Browsers: Chrome

    Test approach
        -This project is use a Agile Methodology with scrum approach for Automation and manual testing. 
        Entry and Exit Criteria:
        Entry:
            Planning Readiness:
                - Test Strategy is complete.
                - Test Plan for the specific test phase is complete.
                - Test Management process and tools are setup and communicated.
                - Defect Management process are setup and communicated.
                - Reporting and related metrics have been developed.
            
            Resource readiness:
                - Test execution plan is prepared and aligned with test resources.
            
            Environment Readiness:
                - Test demo environment API, UI, DB available to shaken out.
                - Test data is in the environment / mechanism to generate test data is established.

            Execution Readiness:
                - Test scripts are in the test management tools,
                - Test scripts and execution plan are aligned with end to end.
                - Defect management sessions / communication channels are setup

       Exit criteria:
            Execution Completion:
                - Test scripts are 100% executed or have agreement to not be included in this test phase.
                - Test execution results are documented.
                - Open defects are resolved or have agreement / workaround to address.x
    
            Reporting Completion:
                - Test Closure Memo is complete.
                - Agreed test metrics for reporting are provided.
      
       Defect Management:
            Defect management is the process of capturing, triaging, fixing, and retesting defects throughout the test execution process. 
            The purpose of a consistent, structured defect lifecycle is to:
                - Provide clarity as to ownership and status of a defect.
                - Ensure all required actions are undertaken with severity and priority
                - Minimise the probability of the same issue appearing in later test phases.
            
            Defect Severity:
                Severity 1: The business impact of the defect is critical.
                            ex- Test environment is not functioning and testing cannot proceed i.e. Log-in failure.
                Severity 2: The entire application(s), components or business functionality will not work, but a business workaround is available.
                            ex: Vital user-interface is not working; however can perform function via native system interface.
                Severity 3: A minor part of the application(s) or business functionality does not work as expected.  The business functionality is nominally compromised.
                            ex: Help function does not work.
                Severity 4: The function does not perform as expected, however business functionality is not compromised.
                            ex: Cosmetic, navigational or similar issues exist.
            
            Defect Priority: Defect priority measure the impact on the overall test schedule of the defect remaining in the application.
                Priority 1: A problem where testing cannot continue.
                            ex: Vital user interface not working, and no access to native system.
                Priority 2: A problem where testing of a significant application component or function cannot continue.
                            ex: Vital user-interface not working; however can perform function via native system interface.
                 Priority 3: A problem that is not severe.
                             ex: Failures with minor and infrequently used functionality.
                Priority 4: A minor problem.
                             ex: Cosmetic, navigational, or similar issues exist

### Resources
    Testing Team:
        - QA Lead: 
            - Acknowledge the completion of a section within a cycle.
            - Give the OK to start next level of testing.
            - Facilitate defect communications between testing team and technical / development team.
        - Test Engineers:
             - Develop test conditions, test cases, expected results, and execution scripts
             - Perform execution and validation. 
             - Identify, document and prioritize defects according to the guidance provided by the Test lead.
             - Prepare testing metrics and provide regular status.
            
    Tools:
        - Playwright for UI and API automation testing.
        - Pycharm IDE for creating Swag Lab automation project. 

### Schedule
| Activity                 | Start Date  | End Date    |
|--------------------------|-------------|-------------|
| Test Planning            | 07/10/2024  | 08/10/2024  |
| Test Design              | 07/10/2024  | 08/10/2024  |
| Test Reporting           | 07/10/2024  | 08/10/202   |

### Test activities
    Test Case Structure
        Test scenarios: Test scenarios are high-level descriptions of functional and technical areas to be tested.  Scenarios can be broken down until detailed, testable conditions and expected results can be determined.  They relate directly to the business processes for the component being tested. 
                        The expectation is that the user stories will represent the different test scenarios.
        Test Conditions:Test conditions (also referred to as test cases) relate directly to the requirements/users stories or specification for the component being tested. 
                        It may be possible to prove multiple test conditions during execution of a scenario.
        Test Scripts:Test data is a key part of the testing phases. It is essential that the data used for testing is representative of the live environment.  
                     Therefore, for the test phases from System Integration Test onward, converted data (i.e. data that was extracted from legacy, transformed, and then loaded into the testing environment) is recommended to be used.
        Test Data: Test data is a key part of the testing phases. It is essential that the data used for testing is representative of the live environment. 
                   Therefore, for the test phases from System Integration Test onward, converted data (i.e. data that was extracted from legacy, transformed, and then loaded into the testing environment) is recommended to be used.
    Automated Test Design:
        Test Data Requirements: Login/Logut, product search, filter, Cart, Checkout.
        Data Management: Maintain .py file all data.

### Test Risks and Mitigation Factors
    Risk: Non-availability of Independent Test environment and accessibility
        Mitigation plan: Due to non availability of the environment, the schedule gets impacted and will lead to delayed start of Test execution. 
        Impact: High

### Environment
     Demo Environment: demo website "https://www.saucedemo.com/" for testing.
        - Browsers: Chrome

### Approval
    This test plan is approved by the following stakeholders:
    