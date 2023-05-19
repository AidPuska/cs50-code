-- Keep a log of any SQL queries you execute as you solve the mystery.
-- found crime reports from that day (theft took place at 10:15) + 10min
SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
-- got more info about theft, got info about car and atm Leggett Street, at the leaving time he called someone and told to get earliest flight for tomorrow, 6am dog
SELECT transcript FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
-- got account numbers and namse, passports, and one of them is from thief
SELECT * FROM bank_accounts JOIN people ON bank_accounts.person_id = people.id WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw');
-- got their names, with passport numbers and phone numbers, got those calls
SELECT * FROM phone_calls WHERE caller IN(SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE license_plate IN (SELECT license_plate FROM bank_accounts JOIN people ON bank_accounts.person_id = people.id WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw')) AND day = 28 AND hour = 10)) AND day = 28;
-- got their flights of people who got on flight on 29 july where passport numbers are from three people
SELECT * FROM passengers JOIN flights ON passengers.flight_id = flights.id JOIN airports ON flights.origin_airport_id = airports.id WHERE city = 'Fiftyville' AND year = 2021 AND month = 7 AND day = 29 AND passengers.passport_number IN (SELECT passport_number FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE caller IN(SELECT phone_number FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE license_plate IN (SELECT license_plate FROM bank_accounts JOIN people ON bank_accounts.person_id = people.id WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw')) AND day = 28 AND hour = 10))AND day = 28));
-- looked again for exiting time from bakery_security_logs and Bruce left
SELECT * FROM bakery_security_logs WHERE license_plate IN (SELECT license_plate FROM bank_accounts JOIN people ON bank_accounts.person_id = people.id WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw')) AND day = 28 AND hour = 10;