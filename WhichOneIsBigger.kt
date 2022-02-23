//내가 짠 코드
import java.util.Scanner

fun main(){
    var sc = Scanner(System.`in`)
    var a = sc.nextInt()//readLine과 달리 공백을 기준으로 입력을 받아줌
    var b = sc.nextInt()

//    if(-10000 <= a || a<= 10000)
//    {
//        if(-10000 <= b || b<= 10000)
//        {
//            if(a>b)
//                println(">")
//            else if(a<b)
//                println("<")
//            else
//                println("==")
//        }
//    }
    when { // 위에꺼를 세 줄로 줄이기 가능
        a>b -> println(">")
        a<b -> println("<")
        else -> println("==")
    }
}
//남이 짠 코드
//import java.io.BufferedReader
//import java.io.InputStreamReader
//import java.util.*
//
//fun main() {
//
//    val br = BufferedReader(InputStreamReader(System.`in`))
//      Reader객체를 생성하여 br 변수에 주소를 할당
//    val token = StringTokenizer(br.readLine())
//      br.readLine()을 통해 정수 두 개를 입력받고 토큰에게 넘겨주면
//      공백을 기준으로 토큰이 split해줌
//    val A = Integer.parseInt(token.nextToken()) A에게 첫번째 토큰을 입력 후 Int로 형변환
//    val B = Integer.parseInt(token.nextToken()) B에게 두번째 토큰을 입력 후 Int로 형변환
//    br.close()
//
//
//    when {
//        A>B -> println(">")
//        A<B -> println("<")
//        else -> println("==")
//    }
//
//}