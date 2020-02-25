package com.example.tsi;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MainActivity";
    Button startButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        configureNextButton();
    }

    private void configureNextButton() {
        startButton = (Button) findViewById(R.id.startButton);
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(MainActivity.this, camera.class));
            }
        });
    }
    private void uploadFile() {
        /*if (selectedFileUri != null) { */
            dialog = new ProgressDialog(MainActivity.this);
            dialog.setProgressStyle(ProgressDialog.STYLE_HORIZONTAL);
            dialog.setMessage("Uploading....");
            dialog.setIndeterminate(false);
            dialog.setMax(100);
            dialog.setCancelable(false);
            dialog.show();

            File file = null;

            //try {
            //System.out.println("trying");
            //System.out.println(selectedFileUri);
            //file = new File(Common.getFilePath(this, selectedFileUri)); //replace with file path @Edward @Imafont
            System.out.println(file);
            System.out.println(file.getClass().getSimpleName());
            System.out.println("I survived");
            //} catch (URISyntaxException e) {
            // e.printStackTrace();
            //}

            if (file != null) {
                final ProgressRequestBody requestBody = new ProgressRequestBody(file, this);

                final MultipartBody.Part body = MultipartBody.Part.createFormData("image", file.getName(), requestBody);

                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        mService.uploadFile(body)
                                .enqueue(new Callback<String>() {
                                    @Override
                                    public void onResponse(Call<String> call, Response<String> response) {
                                        dialog.dismiss();

                                        String image_processed_link = new StringBuilder("http://10.0.2.2:5000/" +
                                                response.body().replace("\"", "")).toString();
                                        Picasso.get().load(image_processed_link)
                                                .into(imageView);
                                        Toast.makeText(MainActivity.this, "Detected!!!", Toast.LENGTH_SHORT);
                                    }

                                    @Override
                                    public void onFailure(Call<String> call, Throwable t) {
                                        dialog.dismiss();
                                        Toast.makeText(MainActivity.this, "" + t.getMessage(), Toast.LENGTH_SHORT).show();
                                    }
                                });

                    }


                }).start();


            } else {
                System.out.println("Not working");
                Toast.makeText(this, "Cannot upload this file!! File is null", Toast.LENGTH_SHORT).show();
            }
        //}
    }

}
