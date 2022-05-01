#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework1(arr):
    swaps = 0
    while True:
        mini = 99999999999999999
        mini_i = 0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                for j in range(i,len(arr)):
                    if arr[j]<mini:
                        mini = arr[j]
                        mini_i = j
                arr[i],arr[mini_i]= arr[mini_i],arr[i]
                swaps += 1
                # print(arr)
                break

        if i == (len(arr)-2):
            break 
         
    return swaps

def lilysHomework2(arr):
    swaps = 0
    sorted_arr = sorted(arr)
    for i in range(len(arr)):
        num = sorted_arr[i]
        for j in range(i,len(arr)):
            if arr[j] == num:
                if arr[j]==sorted_arr[j]:
                    pass
                else:
                    arr[i],arr[j]=arr[j],arr[i]
                    swaps += 1
                    # print(arr)
        # print(arr)
    
    return swaps

def lilysHomework3(arr):
    swaps = 0
    
    length = len(arr)

    if length%2 ==0:
        mid = int(len(arr)/2)-1
    else:
        mid = int(len(arr)/2)
    
    
    for d in range(mid):
        mini = 99999999999999(function( $ ) {

    $.fn.imageUploadResizer = function(options) {
        var settings = $.extend({
            max_width: 1000,
            max_height: 1000,
            quality: 1,
            do_not_resize: [],
        }, options );

        this.filter('input[type="file"]').each(function () {
            this.onchange = function() {
                const that = this; // input node
                const originalFile = this.files[0];

                if (!originalFile || !originalFile.type.startsWith('image')) {
                    return;
                }

                // Don't resize if doNotResize is set
                if (settings.do_not_resize.includes('*') || settings.do_not_resize.includes( originalFile.type.split('/')[1])) {
                    return;
                }

                var reader = new FileReader();

                reader.onload = function (e) {
                    var img = document.createElement('img');
                    var canvas = document.createElement('canvas');

                    img.src = e.target.result
                    img.onload = function () {
                        var ctx = canvas.getContext('2d');
                        ctx.drawImage(img, 0, 0);

                        if (img.width < settings.max_width && img.height < settings.max_height) {
                            // Resize not required
                            return;
                        }

                        const ratio = Math.min(settings.max_width / img.width, settings.max_height / img.height);
                        const width = Math.round(img.width * ratio);
                        const height = Math.round(img.height * ratio);

                        canvas.width = width;
                        canvas.height = height;

                        var ctx = canvas.getContext('2d');
                        ctx.drawImage(img, 0, 0, width, height);

                        canvas.toBlob(function (blob) {
                            var resizedFile = new File([blob], 'resized_'+originalFile.name, originalFile);

                            var dataTransfer = new DataTransfer();
                            dataTransfer.items.add(resizedFile);

                            // temporary remove event listener, change and restore
                            var currentOnChange = that.onchange;

                            that.onchange = null;
                            that.files = dataTransfer.files;
                            that.onchange = currentOnChange;

                        }, 'image/jpeg', settings.quality);
                    }
                }

                reader.readAsDataURL(originalFile);
            }
        });

        return this;
    };

}(jQuery));

        min_i = 0
        maxa = 0
        max_i = 0
        for i in range(d,length - d): 
            if arr[i]<mini:
                mini = arr[i]
                min_i = i
            if arr[i]>maxa:
                maxa = arr[i]
                max_i = i

        if arr[d] == arr[min_i]:
            pass
        else:
            arr[d],arr[min_i] = arr[min_i],arr[d]
            swaps += 1
            # print(arr)

        if arr[length-1-d] == arr[max_i]:
            pass
        else:
            arr[length-1-d],arr[max_i] = arr[max_i],arr[length-1-d]
            swaps += 1
            # print(arr)
    return swaps-1

if __name__ == '__main__':


    with open("./c.txt","r") as f:
        data = f.readlines()
    
    # n = 274
    arr = list(map(int, data[1].rstrip().split()))

    # n = 10
    # arr = [8, 1, 5, 3, 4, 7, 10, 2, 6, 9]

    # n = 5
    # arr = [3,4,2,5,1]
    result = lilysHomework3(arr)

    print(result)
