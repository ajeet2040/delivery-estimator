
# About
The purpose of this file is to have a design for building out the application for the problem statement.

## Problem Statement
Build a delivery service with cost and time estimation based on certain fixed criteria.
> NOTE: For details, please refer to the problem statement document.

## Assumptions
1. For simplicity purpose of the application and as less master data is required, will not be using database here.

## Entities (Model) Design
This section lists out the entities of the application and their attributes(fields).

1. Vehicle

   | Column | Data Type | Description|
   |--------------|-----------|------|
   | id |  text  | unique id for vehicle|
   | max_speed | number | max speed vehicle can travel|
   | max_carriable_weight | number | max weight vehicle can carry|

2. Offer

   | Column | Data Type | Description|
   |--------------|-----------|------|
   | code | text   | unique offer code|
   | min_distance | number | mimimum distance of delivery required for offer to be valid|
   | max_distance | number| maximum distance of delivery required for offer to be valid|
   | min_weight | number| mimimum weight required for offer to be valid|
   | max_weight | number| mimimum weight required for offer to be valid|
   | discount_per | number | discount in percentage of total cost|

3. Package 

   | Column | Data Type | Description|
   |--------------|-----------|-----------|
   | id | text  | unique id for package|
   | weight | number|
   | distance | number|
   | discount_amt | number|
   | offer_code | text | offer code - relates to Offer entity|
   | total_cost | number | offer code - relates to Offer entity|


## Tech Stack
Planning to use below tech stack
1. Python
2. Any python library for CLI

## Initial Code Design
(MAYBE REFINED)

1. Create Dataclass for each entity. Keeping it as separate modules for isolation.
2. Setup module to load master data initially (Offers)
3. Keep Offers master data in a json file
3. One module for each challenge containing the core logic/algorithm.
3. Several test cases for each challenge (TDD)
5. CLI module for accepting inputs and providing outputs
4. Additional unit test cases as per module design.

> NOTE: The methods for each module to be designed as part of the detailed design.

## IDE and Tools
Pycharm Community

