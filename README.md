# delivery-estimator app
CLI app with cost and time estimation for deliveries based on certain fixed criteria.

## Problem Statement
1. Build a command line application to
estimate the total delivery cost of each package with
an offer code (if applicable).
2. Build a command line application to calculate the estimated delivery time for every package by maximizing 
 no. of packages in every shipment.
> NOTE: Detailed information can be found in Problem Statement. (Not including here for now. )

## Prerequisites
 Python3.6+ installed.

## RUN APP
1. For Delivery Cost Estimation App (Challenge 1), Run the below command from root directory. 
    ```
    python run_delivery_cost_estimator.py
    ```
2. For Delivery Time Estimation App (Challenge 2), Run the below command from root directory. 
    ```
    python run_delivery_time_estimator.py
    ```

> NOTE: For linux, use `python3` instead of python. (Ignore if it is linked)

> NOTE: You can use a different offers setup by replacing the path for 'OFFERS_JSON_PATH' in [config.py](config.py) 

## Testing
    
Run the below command from root directory. 
```
python -m unittest discover -s tests -v
```

Refer https://docs.python.org/3/library/unittest.html#command-line-interface for different ways to run.

## Assumptions:
1. The fields: discount, delivery cost are rounded down to two decimal digits.
2. Max limits for no. of packages is set to  and no. of vehicles is set to 10000. (Is configurable via config)
2. Display a user friendly message prompting user to enter data when application is run.
3. Create separate cli scripts for Delivery Cost Estimation(Challenge 1) and Delivery Time Estimation(Challenge 2). 
4. Looks like we have minor typo in Challenge 2 Sample input. Some Offer codes are with double F. 
   Please ignore if not applicable. (different offer codes setup)


## Design Considerations
1. **Offers data is stored in JSON file for simplicity purpose**. For production app, this along will all other entities
    will be stored in database.
2. **Considering Time, not all test cases have been covered. There is scope to add bunch of more test cases : positive and 
   negative for both cost and time calculation logic. (That being said, plan is to add more as per time availability)**
3. The entry scripts `run_delivery_cost_estimator.py` and `run_delivery_time_estimator.py` are designed as python scripts
   to keep a simple flow. Alternate option is to have an OOP design for this.
4. Refer [initial design](docs/initial-design.md) for some pointers on initial design process.
5. For Testing, have utilised the python module `unittest`.

## Scope for Improvements
These are some pointers for improvements.(This is something that can be improved in next iteration.)
1. The logic for Shipments assignment and time calculation can be optimised and refactored(broken down) 
   for better code design. Logic is present in this [module](delivery_shipments_assigner.py)
2. The code in  [utils](utils.py) module follows a simple methods approach for simplicity.
   This can be refactored as various Classes of utils based on their responsibility.
3. Validation for entities can be added at the data class level.
4. The CLI logic for accepting user inputs can be refactored or a suitable python library can be used. 
5. For Testing , input are added as json files for packages. Even output can be added as json files and more robust
   framework can be set up. Also same test case can be run for multiple set of inputs.

## Tech stack
1. Python -  https://www.python.org/
