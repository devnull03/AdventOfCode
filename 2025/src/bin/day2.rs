use advent2025::load_inputs;

fn main() {
    let input: Vec<String> = load_inputs("day2").unwrap();
    let input: Vec<(&str, &str)> = input[0]
        .split(",")
        .map(|e| e.split_once("-").unwrap())
        .collect();
    println!("Day 2: {} lines read", &input.len());
    part1(&input);
    part2(&input);
}

fn part1(input: &Vec<(&str, &str)>) {
    let mut running_total: u64 = 0;
    for line in input {
        let start: u64 = line.0.parse().unwrap();
        let end: u64 = line.1.parse().unwrap();

        // println!("{}", end - start);

        let mut line_total = 0;

        for i in start..=end {
            let i_str = i.to_string();
            if i_str.len() % 2 != 0 {
                continue;
            };
            let e = i_str.split_at(i_str.len() / 2);
            if e.0 != e.1 {
                continue;
            }
            // println!("{i}");
            line_total += i
        }
        running_total += line_total;
    }
    println!("part 1: {running_total}");
}

fn part2(input: &Vec<(&str, &str)>) {
    let mut running_total: u64 = 0;
    fn uhhh(num: &str, split_n: usize) -> bool {
        if num.len() == 0 || num.len() < split_n {
            return false;
        }
        if num.len() % split_n != 0 {
            return uhhh(num, split_n + 1);
        }
        let mut e = num.as_bytes().chunks(num.len() / split_n);
        let e_first = e.next().unwrap();
        if e.all(|sub| sub == e_first) {
            true
        } else if num.len() == split_n {
            false
        } else {
            uhhh(num, split_n + 1)
        }
    }
    for line in input {
        let start: u64 = line.0.parse().unwrap();
        let end: u64 = line.1.parse().unwrap();

        let mut range_total = 0;

        for i in start..=end {
            let i_str = i.to_string();
            if uhhh(&i_str, 2) {
                range_total += i;
            }
        }
        running_total += range_total;
    }
    println!("part 2: {running_total}");
}
