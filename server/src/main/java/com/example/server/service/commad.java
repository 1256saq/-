package com.example.server.service;

import java.io.IOException;
import java.util.List;

public class commad {
    public void excute(List<String> cmd){
        try {
            Process process = new ProcessBuilder(cmd).start();
            process.waitFor();
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
