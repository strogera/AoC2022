import java.io.File

fun main(){
    val elves = File("input.txt").readText().split("\r\n\r\n").map{it.lines().sumOf{it.toInt()}}.sorted()
    println(elves.last())
    println(elves.takeLast(3).sum())
}