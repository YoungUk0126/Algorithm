import java.util.*

fun main()
{
    var sc = Scanner(System.`in`)
    var n = sc.nextInt()
    var x = sc.nextInt()

    //var seq = IntArray(n) { readLine()!!.toInt() } // 반복해서 n만큼 배열에 입력받음
    var seq = IntArray(n, {0})

    for(i in 0 until n)
    {
        seq[i] = sc.nextInt()//이렇게 간단하게 공백으로 입력이 된다니...아까는 안됐는데 뭐지
    }
    for(i in 0 until n)
    {
        if(seq[i] < x)
            print("${seq[i]} ")//${}으로 문자열 안에 변수 바로 사용
    }
}
