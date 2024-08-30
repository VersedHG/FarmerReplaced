while True:
	if get_pos_x() == 0:
		if get_pos_y() != 2:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
		else:
			if can_harvest():
				harvest()
				plant(Entities.Bush)
			move(East)
		move(North)
	elif get_pos_x() == 1:
		if get_pos_y() != 2:
			if can_harvest():
				harvest()
		else:
			if can_harvest():
				harvest()
			move(East)
		move(North)
	elif get_pos_x() == 2:
		if get_pos_y() != 3:
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Turf:
				till()
			if num_items(Items.Carrot_Seed) < 1:
				trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
		else:
			if can_harvest():
				harvest()
			if get_entity_type() == Grounds.Turf:
				till()
			if num_items(Items.Carrot_Seed) < 1:
				trade(Items.Carrot_Seed)
			plant(Entities.Carrots)
			move(East)
		move(North)
