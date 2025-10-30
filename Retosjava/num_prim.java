package Retosjava;

import java.util.Scanner;

public class num_prim {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Escribe un número: ");
        int num = scanner.nextInt();
        System.out.println(num % 6);

        if ( num == 1){
            System.out.println("El número es primo");
        }

        else{
            for(int i = num; i >= 0; i--){
                if( i % 6 == 0 && i % 2 == 0 && i % 3 == 0){
                    System.out.println("No es primo :(");
                }
                if( i % 6 == 0 || i % 2 == 0 || i % 3 == 0){
                    System.out.println("No es primo :(");
                }
            }
            System.out.println("Happe");
        }
        
        
        

    }
}