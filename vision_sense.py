include <iostream>
include <vector>

extern "C" {
    struct Pixel {
        unsigned char r, g, b;
    };

    bool is_dark_image(Pixel* data, int width, int height, int threshold) {
        long long total_brightness = 0;
        int num_pixels = width * height;

        for (int i = 0; i < num_pixels; ++i) {
            total_brightness += (data[i].r + data[i].g + data[i].b) / 3;
        }

        double avg = total_brightness / (double)num_pixels;
        return avg < threshold;
    }

    int detect_movement(Pixel* frame1, Pixel* frame2, int width, int height) {
        int changes = 0;
        int num_pixels = width * height;
        
        for (int i = 0; i < num_pixels; ++i) {
            int diff = abs(frame1[i].r - frame2[i].r) +
                       abs(frame1[i].g - frame2[i].g) +
                       abs(frame1[i].b - frame2[i].b);
            if (diff > 50) changes++;
        }
        return changes;
    }
}
