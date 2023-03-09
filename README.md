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
- [ ] Property
    1. [ ] Pictures
    2. [ ] Name
    3. [ ] Address
    4. [ ] Date Range
    5. [ ] Number of guests
    6. [ ] Beds & Baths
    7. [ ] Amenities
    8. [ ] Description
    9. [ ] Owner

- [ ] User (inherited from AbstractUser)
    1. [x] first name
    2. [x] last name
    3. [x] username
    4. [ ] avatar
    5. [x] password
    6. [ ] phone number
    7. [x] email
    8. [ ] date of birth

- [ ] Reservation
    1. [ ] user
    2. [ ] status
    3. [ ] property

## Tests to add