fun main(){
    var a = readLine()!!.toInt()
    var b = readLine()!!.toString()//b[0]식으로 요소로 접근하려면 toString이라고 명시해야함

    //println(b[0] - '0')//char형을 int로 바꿔주는 식

    println(a*(b[2] - '0'))
    println(a*(b[1] - '0'))
    println(a*(b[0] - '0'))

    println(a*b.toInt())


}