use std::fs;

fn main() {
    let input = fs::read_to_string("./input.txt").expect("input file not found");
    let mut lines: Vec<i32> = input
        .split("\r\n\r\n")
        .map(|c| c.split("\r\n").map(|l| l.parse::<i32>().unwrap()).sum())
        .collect();
    lines.sort_unstable();
    println!("{}\n{}",  lines.last().unwrap(),   lines.iter().rev().take(3).sum::<i32>());
}
