import java.lang.System.exit

fun main(){
    var score = readLine()!!.toInt()
    if(score<0 || score>100)
    {
        println("Out of range")
        exit(0)
    }else {
        when (score) {
            in 90..100 -> println("A")
            in 80..90 -> println("B")
            in 70..80 -> println("C")
            in 60..70 -> println("D")
            else -> println("F")
        }
    }
}