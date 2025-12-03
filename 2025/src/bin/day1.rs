use advent2025::load_inputs;

fn main() {
    let input: Vec<String> = load_inputs("day1").unwrap();
    println!("Day 1: {} lines read", input.len());
    part1(&input);
    part2(&input);
    // part2_retarded(&input);
}

fn part1(input: &Vec<String>) {
    // println!("Day 1: {} lines read", input.len());

    let mut zero_counter: i32 = 0;
    let mut current_position: i32 = 50;

    for line in input {
        let mut line_chars = line.chars();
        let direction: i32 = if line_chars.next().unwrap() == 'L' {
            -1
        } else {
            1
        };
        let distance: i32 = line_chars.collect::<String>().parse().unwrap();
        let line_calc = (&current_position + (direction * distance % 100)) % 100;
        current_position = line_calc;
        if line_calc == 0 {
            zero_counter += 1
        };
    }
    println!("part 1 = {:?}", zero_counter);
}

fn part2(input: &Vec<String>) {
    let mut zero_counter: i32 = 0;
    let mut current_position: i32 = 50;

    for line in input {
        let mut line_chars = line.chars();
        let direction: i32 = if line_chars.next().unwrap() == 'L' {
            -1
        } else {
            1
        };
        let distance: i32 = line_chars.collect::<String>().parse().unwrap();
        let new_position = if direction > 0 {
            zero_counter += (current_position + distance) / 100;
            (current_position + distance) % 100
        } else {
            let reversed = (100 - current_position) % 100;
            zero_counter += (reversed + distance) / 100;
            (current_position - distance).rem_euclid(100)
        };

        current_position = new_position;
    }
    println!("part 2 = {:?}", zero_counter);
}

fn part2_retarded(input: &Vec<String>) {
    // println!("Day 1: {} lines read", input.len());

    let mut zero_counter: i32 = 0;
    let mut current_position: i32 = 50;

    for line in input {
        let mut line_chars = line.chars();
        let direction: i32 = if line_chars.next().unwrap() == 'L' {
            -1
        } else {
            1
        };
        let distance: i32 = line_chars.collect::<String>().parse().unwrap();

        let new_position = (&current_position + (direction * distance % 100)) % 100;

        let mut temp_pos_counter = current_position;

        for _ in 0..distance {
            temp_pos_counter += direction;
            match temp_pos_counter {
                -1 => temp_pos_counter = 99,
                100 => temp_pos_counter = 0,
                0 => zero_counter += 1,
                _ => {}
            }
        }

        current_position = new_position;
    }
    println!("day 2 retarded = {:?}", zero_counter);
}
