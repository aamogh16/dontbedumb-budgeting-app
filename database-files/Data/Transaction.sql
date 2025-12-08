CREATE TABLE Transaction (
   transactionID INT PRIMARY KEY AUTO_INCREMENT,
   amount INT NOT NULL,
   date DATETIME NOT NULL,
   description VARCHAR(300),
   method VARCHAR(100),
   source VARCHAR(100),
   accountID INT NOT NULL,
   categoryID INT,
   FOREIGN KEY (accountID) REFERENCES Account(acctID) ON DELETE CASCADE,
   FOREIGN KEY (categoryID) REFERENCES Category(categoryID) ON DELETE SET NULL
);

insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (15847, 450, '2024-11-15 14:23:45', 'Grocery shopping at Whole Foods', 'Credit Card', 'Whole Foods Market', 1, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (28392, 1200, '2024-11-20 09:15:30', 'Monthly rent payment', 'Bank Transfer', 'Property Management', 2, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (39567, 85, '2024-11-22 18:45:12', 'Dinner at Italian restaurant', 'Debit Card', 'Bella Italia', 3, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (47821, 2500, '2024-11-25 11:30:00', 'Car insurance premium', 'Check', 'State Farm', 4, '89-264-7590');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (52934, 175, '2024-11-28 16:20:33', 'Utility bill payment', 'Online Payment', 'Electric Company', 5, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (64189, 95, '2024-11-30 13:45:18', 'Gas station fill-up', 'Credit Card', 'Shell', 6, '89-264-7590');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (75423, 320, '2024-12-01 10:12:45', 'Clothing purchase', 'Debit Card', 'Macy''s', 7, '28-697-0598');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (86758, 55, '2024-12-02 19:30:22', 'Movie tickets', 'Credit Card', 'AMC Theaters', 8, '70-074-2267');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (97264, 680, '2024-12-03 08:45:00', 'Laptop repair', 'Credit Card', 'Best Buy', 9, '58-476-1815');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (10573, 42, '2024-12-04 12:15:38', 'Coffee and breakfast', 'Cash', 'Starbucks', 10, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (21896, 1500, '2024-12-05 15:00:00', 'Dental cleaning and checkup', 'Credit Card', 'Smile Dental', 11, '24-200-3936');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (33274, 220, '2024-12-06 11:45:27', 'Gym membership', 'Bank Transfer', 'Gold''s Gym', 12, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (44682, 380, '2024-12-07 14:30:15', 'Grocery shopping', 'Debit Card', 'Trader Joe''s', 13, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (55918, 125, '2024-11-10 17:20:44', 'Pet supplies', 'Credit Card', 'Petco', 14, '48-325-6972');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (67245, 2100, '2024-11-12 09:00:00', 'Tuition payment', 'Check', 'University', 15, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (78591, 65, '2024-11-14 20:15:30', 'Takeout dinner', 'Credit Card', 'Chipotle', 16, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (89327, 450, '2024-11-16 13:40:22', 'Home internet bill', 'Online Payment', 'Comcast', 17, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (91864, 280, '2024-11-18 10:25:18', 'Pharmacy prescription', 'Debit Card', 'CVS Pharmacy', 18, '24-200-3936');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (12459, 150, '2024-11-19 16:50:00', 'Haircut and styling', 'Cash', 'Style Salon', 19, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (23785, 95, '2024-11-21 12:30:45', 'Office supplies', 'Credit Card', 'Staples', 20, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (35142, 720, '2024-11-23 08:15:30', 'Plane ticket', 'Credit Card', 'Delta Airlines', 21, '89-264-7590');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (46897, 55, '2024-11-24 19:45:12', 'Streaming subscription', 'Auto-Pay', 'Netflix', 22, '58-476-1815');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (58263, 340, '2024-11-26 14:20:00', 'New shoes', 'Debit Card', 'Nike Store', 23, '28-697-0598');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (69534, 180, '2024-11-27 11:05:38', 'Car wash and detailing', 'Credit Card', 'Auto Spa', 24, '89-264-7590');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (70821, 420, '2024-11-29 15:30:22', 'Furniture purchase', 'Credit Card', 'IKEA', 25, '83-634-7153');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (82175, 78, '2024-12-01 18:15:45', 'Fast food lunch', 'Debit Card', 'McDonald''s', 26, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (93468, 1250, '2024-12-02 10:00:00', 'HOA fees', 'Bank Transfer', 'HOA Management', 27, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (14792, 165, '2024-12-03 13:25:30', 'Books purchase', 'Credit Card', 'Barnes & Noble', 28, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (26384, 520, '2024-12-04 09:40:18', 'Car maintenance', 'Debit Card', 'Jiffy Lube', 29, '89-264-7590');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (37619, 95, '2024-12-05 17:55:00', 'Concert tickets', 'Credit Card', 'Ticketmaster', 30, '70-074-2267');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (48257, 310, '2024-12-06 12:10:45', 'Veterinary visit', 'Credit Card', 'Animal Hospital', 31, '48-325-6972');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (59873, 145, '2024-12-07 15:35:22', 'Garden supplies', 'Cash', 'Home Depot', 32, '15-560-8627');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (61425, 890, '2024-11-08 08:20:00', 'Laptop purchase', 'Credit Card', 'Apple Store', 33, '58-476-1815');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (72698, 62, '2024-11-09 19:45:30', 'Pizza delivery', 'Credit Card', 'Domino''s Pizza', 34, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (84931, 275, '2024-11-11 11:30:18', 'Home security system', 'Bank Transfer', 'ADT', 35, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (96174, 185, '2024-11-13 14:15:45', 'Spa treatment', 'Debit Card', 'Serenity Spa', 36, '24-200-3936');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (17582, 95, '2024-11-15 10:40:00', 'Phone accessories', 'Credit Card', 'Best Buy', 37, '58-476-1815');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (28914, 1350, '2024-11-17 16:25:30', 'Property tax', 'Check', 'County Tax Office', 38, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (30247, 420, '2024-11-19 12:50:18', 'Smart TV purchase', 'Credit Card', 'Target', 39, '58-476-1815');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (41569, 85, '2024-11-21 18:10:45', 'Sushi dinner', 'Debit Card', 'Tokyo Sushi', 40, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (52836, 210, '2024-11-22 09:35:22', 'Running shoes', 'Credit Card', 'Foot Locker', 41, '28-697-0598');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (64192, 1680, '2024-11-24 13:00:00', 'Orthodontist payment', 'Check', 'Orthodontics Center', 42, '24-200-3936');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (75428, 325, '2024-11-26 15:45:30', 'Winter coat', 'Credit Card', 'North Face', 43, '28-697-0598');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (86751, 140, '2024-11-28 11:20:18', 'Wine purchase', 'Cash', 'Total Wine', 44, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (98365, 560, '2024-11-30 14:55:45', 'Kitchen appliances', 'Debit Card', 'Williams Sonoma', 45, '83-634-7153');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (19724, 95, '2024-12-01 17:30:00', 'Yoga mat and equipment', 'Credit Card', 'Lululemon', 46, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (20186, 780, '2024-12-02 10:15:30', 'Flight and hotel booking', 'Credit Card', 'Expedia', 47, '89-264-7590');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (31594, 125, '2024-12-03 13:40:18', 'Art supplies', 'Debit Card', 'Michael''s', 48, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (42827, 245, '2024-12-04 16:25:45', 'Professional headshots', 'Check', 'Photo Studio', 49, '42-562-0760');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (54163, 370, '2024-12-05 09:50:22', 'Eyeglasses purchase', 'Credit Card', 'LensCrafters', 50, '24-200-3936');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (65498, 88, '2024-12-06 19:15:00', 'Thai food delivery', 'Credit Card', 'Thai Express', 51, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (76832, 1200, '2024-12-07 11:40:30', 'New mattress', 'Debit Card', 'Mattress Firm', 52, '83-634-7153');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (87945, 195, '2024-11-05 14:25:18', 'Baby supplies', 'Credit Card', 'Buy Buy Baby', 53, '48-325-6972');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (99271, 425, '2024-11-07 10:10:45', 'Bicycle purchase', 'Cash', 'REI', 54, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (10638, 75, '2024-11-09 17:55:22', 'Ice cream shop', 'Debit Card', 'Cold Stone', 55, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (21974, 920, '2024-11-11 13:30:00', 'Photography equipment', 'Credit Card', 'B&H Photo', 56, '42-562-0760');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (33285, 165, '2024-11-13 16:15:30', 'Museum membership', 'Bank Transfer', 'Science Museum', 57, '70-074-2267');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (44617, 540, '2024-11-15 12:40:18', 'Tailoring services', 'Check', 'Expert Tailor', 58, '28-697-0598');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (55923, 280, '2024-11-17 15:25:45', 'Gaming console', 'Credit Card', 'GameStop', 59, '70-074-2267');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (67258, 95, '2024-11-19 18:50:22', 'Bakery purchase', 'Cash', 'Local Bakery', 60, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (78549, 1450, '2024-11-21 09:15:00', 'Refrigerator repair', 'Debit Card', 'Appliance Repair Co', 61, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (89834, 210, '2024-11-23 14:40:30', 'Dry cleaning', 'Credit Card', 'Clean & Press', 62, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (91162, 385, '2024-11-25 11:25:18', 'Paint and supplies', 'Cash', 'Sherwin-Williams', 63, '15-560-8627');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (12487, 125, '2024-11-27 16:10:45', 'Board games', 'Credit Card', 'Game Store', 64, '23-983-6981');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (23796, 670, '2024-11-29 13:55:22', 'Jewelry purchase', 'Debit Card', 'Kay Jewelers', 65, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (35124, 190, '2024-12-01 10:30:00', 'Car rental', 'Credit Card', 'Enterprise', 66, '89-264-7590');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (46851, 85, '2024-12-02 18:15:30', 'Sandwich shop lunch', 'Cash', 'Subway', 67, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (58297, 1120, '2024-12-03 15:40:18', 'Computer monitor', 'Credit Card', 'Dell', 68, '58-476-1815');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (69573, 245, '2024-12-04 12:25:45', 'Fitness tracker', 'Debit Card', 'Fitbit Store', 69, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (70918, 460, '2024-12-05 09:10:22', 'Luggage set', 'Credit Card', 'Samsonite', 70, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (82346, 95, '2024-12-06 17:55:00', 'Magazine subscription', 'Bank Transfer', 'Time Magazine', 71, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (93671, 340, '2024-12-07 14:30:30', 'Kitchen cookware', 'Cash', 'Sur La Table', 72, '83-634-7153');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (14925, 525, '2024-11-02 11:15:18', 'Sound system', 'Credit Card', 'Bose', 73, '23-788-2663');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (26389, 175, '2024-11-04 16:40:45', 'Barber shop', 'Cash', 'Classic Cuts', 74, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (37652, 980, '2024-11-06 13:25:22', 'Sectional sofa', 'Debit Card', 'Ashley Furniture', 75, '83-634-7153');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (48914, 65, '2024-11-08 19:10:00', 'Bubble tea', 'Credit Card', 'Boba Shop', 76, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (50287, 1350, '2024-11-10 10:55:30', 'Air conditioning repair', 'Check', 'HVAC Services', 77, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (61543, 290, '2024-11-12 15:30:18', 'Ski equipment', 'Credit Card', 'Sports Authority', 78, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (72896, 115, '2024-11-14 12:15:45', 'Craft supplies', 'Debit Card', 'Hobby Lobby', 79, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (84127, 735, '2024-11-16 09:40:22', 'Dining room table', 'Cash', 'Crate & Barrel', 80, '83-634-7153');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (95461, 185, '2024-11-18 17:25:00', 'Rock climbing gear', 'Credit Card', 'REI', 81, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (16798, 420, '2024-11-20 14:10:30', 'Vacuum cleaner', 'Debit Card', 'Dyson Store', 82, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (28134, 95, '2024-11-22 11:55:18', 'Florist purchase', 'Cash', 'Blooms & Petals', 83, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (39465, 560, '2024-11-24 16:30:45', 'Power tools', 'Credit Card', 'Lowe''s', 84, '15-560-8627');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (40827, 245, '2024-11-26 13:15:22', 'Leather jacket', 'Debit Card', 'Wilson Leather', 85, '28-697-0598');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (52193, 1840, '2024-11-28 10:00:00', 'Washer and dryer', 'Credit Card', 'Sears', 86, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (63529, 88, '2024-11-30 18:45:30', 'Indian food takeout', 'Cash', 'Taj Mahal', 87, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (74856, 375, '2024-12-01 15:20:18', 'Smart watch', 'Debit Card', 'Garmin', 88, '58-476-1815');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (86192, 210, '2024-12-02 12:05:45', 'Camping gear', 'Credit Card', 'Bass Pro Shops', 89, '47-892-8581');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (97528, 125, '2024-12-03 19:50:22', 'Seafood restaurant', 'Cash', 'Red Lobster', 90, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (18754, 890, '2024-12-04 09:35:00', 'Treadmill purchase', 'Credit Card', 'NordicTrack', 91, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (29681, 155, '2024-12-05 16:20:30', 'Party supplies', 'Debit Card', 'Party City', 92, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (30947, 645, '2024-12-06 13:05:18', 'Wireless headphones', 'Credit Card', 'Sony Store', 93, '23-788-2663');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (42215, 270, '2024-12-07 10:50:45', 'Dog grooming', 'Cash', 'Pet Grooming Salon', 94, '48-325-6972');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (53584, 1125, '2024-11-01 15:35:22', 'Home security cameras', 'Debit Card', 'Ring', 95, '75-308-1636');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (64912, 95, '2024-11-03 12:20:00', 'Mexican restaurant', 'Credit Card', 'Chipotle', 96, '77-802-7219');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (76247, 430, '2024-11-05 17:05:30', 'Office chair', 'Cash', 'Office Depot', 97, '35-969-8244');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (87593, 185, '2024-11-07 14:50:18', 'Tennis racket', 'Debit Card', 'Tennis Warehouse', 98, '49-396-8802');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (98826, 765, '2024-11-09 11:35:45', 'Patio furniture set', 'Credit Card', 'Wayfair', 99, '83-634-7153');
insert into Transaction (transactionID, amount, date, description, method, source, accountID, categoryID) values (19158, 340, '2024-11-11 18:20:22', 'Standing desk', 'Cash', 'Uplift Desk', 100, '35-969-8244');