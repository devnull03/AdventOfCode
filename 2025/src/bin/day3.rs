#[allow(unused, unused_variables)]
use advent2025::load_inputs;

fn main() {
    let input: Vec<String> = load_inputs("day3").unwrap();
    println!("Day 3: {} lines read", input.len());
    part1(&input);
    part2(&input);
}

fn uhhh(input: &Vec<String>, req_batteries: usize) -> u64 {
    let mut running_total = 0;

    for line in input {
        let line_bytes = line.as_bytes();
        let mut max_counter: Vec<(usize, u8)> = Vec::new();
        let mut start = 0;

        for b in 0..req_batteries {
            let window = &line_bytes[start..=(line_bytes.len() - req_batteries + b)];
            let mut cur_max = (0, 0);

            for w in 0..window.len() {
                if window[w] > cur_max.1 {
                    cur_max = (w, window[w]);
                }
            }

            start += cur_max.0 + 1;
            max_counter.push(cur_max);
        }

        let number: u64 = String::from_utf8(max_counter.iter().map(|v| v.1).collect())
            .unwrap()
            .parse()
            .unwrap();

        // println!("{:?}", line);
        // println!("{:?}\n---", number);

        running_total += number;
    }
    running_total
}

fn part1(input: &Vec<String>) {
    println!("part1: {}", uhhh(input, 2));
}

fn part2(input: &Vec<String>) {
    println!("part2: {}", uhhh(input, 12));
}
