# CSC309 Restify Group Project

## Endpoints To add
- [x] login & logout (token authentication)
- [x] create profile
- [x] update profile
- [x] login & logout (token authentication)
- [x] create profile
- [x] update profile
- [ ] (OPTIONAL) view profile

- [x] create property
- [x] update property
- [x] delete property
- [ ] (OPTIONAL) view property details

- [x] property list
    - [x] Filters
        1. [x] location
        2. [x] date range
        3. [x] price range
        4. [x] number of guests
    - [x] Order-By
        1. [x] price
        2. [x] start date

- [ ] reservations list (with filters)
    1. [ ] user type
    2. [ ] state

- [ ] status actions
    1. [ ] reserve
    2. [ ] cancel
    3. [ ] approve/ deny pending request
    4. [ ] approve/ deny cancellation request
    5. [ ] terminate

- [ ] view guest comments
- [ ] view property comments
- [ ] create guest comment
- [ ] create property comment

- [ ] list of notifications
- [ ] read notif and clear

## Models to add
- [x] Property
    1. [x] Pictures
    2. [x] Address *
    3. [x] Date Range *
    4. [x] Number of guests *
    5. [x] Beds & Baths *
    6. [x] Amenities
    7. [x] Description
    8. [x] Owner *

- [x] User (inherited from AbstractUser)
    1. [x] first name
    2. [x] last name
    3. [x] username *
    4. [x] avatar
    5. [x] password *
    6. [x] phone number *
    7. [x] email
    8. [x] date of birth
    8. [x] is host *

- [x] Reservation
    1. [x] user *
    2. [x] status *
    3. [x] property *

- [x] Comments
    1. [x] author *
    2. [x] parent *
    3. [x] content *

- [x] Notifications
    1. [x] User *
    2. [x] Content *

### \* mandetory fields

## Tests to add