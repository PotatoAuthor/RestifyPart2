# CSC309 Restify Group Project

## Endpoints To add
- [x] login & logout (token authentication)
- [x] create profile
- [x] update profile
- [ ] (OPTIONAL) view profile

- [x] create property
- [x] update property
- [x] delete property
- [ ] (OPTIONAL) view property details

- [ ] property list
    - [ ] Filters
        1. [ ] location
        2. [ ] date range
        3. [ ] price range
        4. [ ] number of guests
    - [ ] Order-By
        1. [ ] price
        2. [ ] start date

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

- [x] UserComments
    1. [x] commenter *
    2. [x] user *
    3. [x] content *

- [x] PropertyComments
    1. [x] commenter *
    2. [x] property *
    3. [x] content *

- [x] Notifications
    1. [x] User *
    2. [x] Content *

### \* mandetory fields

## Tests to add