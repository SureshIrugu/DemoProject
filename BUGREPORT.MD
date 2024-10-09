****************************BUG REPORT****************************
 Bug Summary
| **Bug ID** | **Summary**                      | **Severity** | **Priority** | **Status**  | **Assigned To**    |
|------------|----------------------------------|--------------|---------------|-------------|------------------ |
| 001        | Checkout process fails           | Critical     | High          | Open        | [Dev_1]           |
| 002        | Product is not loading on page   | Major        | High          | Open        | [Dev_2]           |
| 003        | Warning message is not displaying| Minor        | Medium        | Open        | [Dev_3]           |
| 004        | Product quantity is not updating | Major        | Medium        | Open        | [Dev_4]           |

## Bug Details
Bug ID 1:

    Summary: Checkout process fails.
    Description: The application crashes during the checkout process.
    Steps to reproduce:
        1. Log into "https://www.saucedemo.com/" application with valid credentials.
        2. Select and add item into cart.
        3. Proceed to checkout
        4. Complete the checkout form
        5. Click on Submit

    Expected Result: Checkout should complete successfully. 
    Actual Result: Application is crashed with a 500 error.
    Envrionment: Chrome, Mac.
    Severity: Critial
    Priority: High

Bug ID 2:
    
    Summary: Product is not loading on page.
    Description: Products fail to load after logging in.
    Steps to reproduce:
        1. Hit url "https://www.saucedemo.com/" in Safari browser.
        2. Log with valid credentials.
        3. Observe the product page.

    Expected Result: Products should load and display.
    Actual Result: Products do not appear; loading spinner remains indefinitely.
    Environment: Safari, Mac.
    Severity: Major
    Priority: High


Bug ID 3:

    Summary: Warning message is not displaying
    Description: Checkout fail to validate and display warning message without any product added.
    Steps to reproduce:
         1. Hit url "https://www.saucedemo.com/" in Chrome browser.
         2. Log with valid credentials.
         3. Click on Cart Image, make sure no product added.
         4. Click on Checkout.

    Expected Result: Warning message should display to add product.
    Actual Result: Checkout is successful without any warning message.
    Severity: Minor
    Priority: Medium

But ID 4:

    Summary: roduct quantity is not updating 
    Description: Items added to the cart do not allow to update the quantity.
    Steps to reproduce:
         1. Hit url "https://www.saucedemo.com/" in Chrome browser.
         2. Log with valid credentials.
         3. Select and add item into Cart.
         4. Click on Cart.
         5. Update the quanity. 

    Expected Result: Quantity should allow to increase or decrease.
    Actual Result: Unable to update the quanity.
    Severity: Major
    Priority: Medium
