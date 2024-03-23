// 1. ----------------------------------------------------------------------------------------------------

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
        char symbol = '7';
        int result = (int)symbol - (int)'0';
        System.out.println((int)result);
  }
}

// 2. --------------------------------------------------------------------------------------------------

         import java.time.LocalDateTime;  

          public class CurrentTime {  

                        public static void main(String[] args) {  

                                 LocalDateTime time_now = LocalDateTime.now();  

                                 System.out.println(time_now);  

             }

        }

// 3. ------------------------------------------------------------------------------------------------------


import java.time.LocalDate;

public class DayOfTheMonth {

          public static void main(String[] args) {

                   LocalDate this_day = LocalDate.now();

                   int day_of_month = this_day.getDayOfMonth(); 

                   System.out.println("The day of the month is: " + day_of_month);

    }

}


// 4. -------------------------------------------------------------------------------------------------------


import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    String nextWord = "Z";



    String upperWord = nextWord.toUpperCase();



    if( upperWord.compareTo("N") < 0 ){

        System.out.println("First half of the alphabet");

    }else{

        System.out.println("Second half of the alphabet");

    }

  }

}

// --------------------------------------------------------------------------------------------------------------
