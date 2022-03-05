import java.util.Scanner

fun main(){
    var sc = Scanner(System.`in`)
    var f_dice = sc.nextInt()
    var s_dice = sc.nextInt()
    var t_dice = sc.nextInt()


    if(f_dice == s_dice && s_dice == t_dice)
        println(10000+f_dice*1000)
    else if(f_dice == s_dice || s_dice == t_dice || t_dice == f_dice)
    {
        when
        {
            f_dice == s_dice -> println(1000+f_dice*100)
            s_dice == t_dice -> println(1000+s_dice*100)
            t_dice == f_dice -> println(1000+t_dice*100)
        }
    }
    else
    {
        if(f_dice > s_dice)
            println(f_dice * 100)
        else if(s_dice > t_dice)
            println(s_dice * 100)
        else
            println(t_dice * 100)
    }
}
