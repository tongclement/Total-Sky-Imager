package com.example.androidclientpythonupload2.Utils;

import android.os.Handler;
import android.os.Looper;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.File;

import okhttp3.MediaType;
import okhttp3.RequestBody;
import okio.BufferedSink;

public class ProgressRequestBody extends RequestBody {

    private File file;
    private IUploadCallbacks listener;
    private static int DEFAULT_BUFFER_SIZE = 4096;


    public ProgressRequestBody(File file, IUploadCallbacks listener) {
        this.file = file;
        this.listener = listener;
    }

    @Override
    public MediaType contentType() {
        return MediaType.parse("image/*"); //only accepy image
    }

    @Override
    public void writeTo(BufferedSink sink) throws IOException {
            long fileLength = file.length();
            byte[] buffer = new byte[DEFAULT_BUFFER_SIZE];
        FileInputStream in = new FileInputStream(file);
        long uploaded=0;
        try{
            int read;
            Handler handler = new Handler(Looper.getMainLooper());
            while((read=in.read(buffer)) != -1) {
                //handler.post((Runnable) new ProgressUpdater(uploaded,fileLength));
                handler.post(new ProgressUpdater(uploaded,fileLength));
                uploaded+=read;
                sink.write(buffer, 0,read);
            }

        }finally {
            in.close();
        }

    }

    private class ProgressUpdater implements Runnable{
        private long uploaded;
        private long fileLength;


        public ProgressUpdater(long uploaded, long fileLength) {
            System.out.println("survived 1");
            this.uploaded = uploaded;
            this.fileLength = fileLength;
            System.out.println("survived 2");
        }

        //@Override
        public void run() {
            System.out.println("survived 3");
            listener.onProgressUpdate((int) ((100 * uploaded / fileLength)));
            System.out.println("survived 4");
        }
    }
}
