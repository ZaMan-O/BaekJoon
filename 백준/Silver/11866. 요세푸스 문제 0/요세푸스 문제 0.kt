import java.util.Scanner

fun main() {
    val sc = Scanner(System.`in`)
    val people = sc.nextInt()
    val step = sc.nextInt()
    
    var front = -1
    var queue = mutableListOf<Int>()
    
    for (i in 1..people) {
        queue.add(i)
    }
    print("<")
    for(i in 1..people) {
      for(ii in 1..step-1) {
        queue.add(queue[++front])
      }
      print(queue[++front])
      if(i == people) continue
      print(", ")
    }
    print(">")
}