package com.example.cli;

public class Main {
    public static void main(String[] args) {
        System.out.println("CLI Application Started");
        
        if (args.length > 0) {
            System.out.println("Arguments: " + String.join(", ", args));
        } else {
            printHelp();
        }
    }
    
    private static void printHelp() {
        System.out.println("Usage: java -jar maven-cli-app.jar [options]");
        System.out.println("Options:");
        System.out.println("  --help    Show this help message");
        System.out.println("  --version Show version information");
    }
}
