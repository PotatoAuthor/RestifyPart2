# CSC309 Restify Group Project

## Endpoints To add
- [ ] login & logout (token authentication)
- [ ] create profile
- [ ] update profile
- [ ] (OPTIONAL) view profile

- [ ] create property
- [ ] update property
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
    2. [x] Address
    3. [x] Date Range
    4. [x] Number of guests
    5. [x] Beds & Baths
    6. [x] Amenities
    7. [x] Description
    8. [x] Owner

- [x] User (inherited from AbstractUser)
    1. [x] first name
    2. [x] last name
    3. [x] username
    4. [x] avatar
    5. [x] password
    6. [x] phone number
    7. [x] email
    8. [x] date of birth

- [x] Reservation
    1. [x] user
    2. [x] status
    3. [x] property

- [ ] UserComments
    1. [ ] commenter
    2. [ ] user
    3. [ ] content

- [ ] PropertyComments
    1. [ ] commenter
    2. [ ] property
    3. [ ] content

## Tests to add