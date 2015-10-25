/*
 * Microsoft grants you the right to use these script files for the sole purpose of either: 
 * (i) interacting through your browser with the Microsoft website, subject to the website’s 
 * terms of use; or (ii) using the files as included with a Microsoft product subject to that
 * product’s license terms. Microsoft reserves all other rights to the files not expressly 
 * granted by Microsoft, whether by implication, estoppel or otherwise. The notices and 
 * licenses below are for informational purposes only.
*/
/*
 * Provided for Informational Purposes Only
 * jQuery Easing v1.3 - http://gsgd.co.uk/sandbox/jquery/easing/
 *
 * Uses the built in easing capabilities added In jQuery 1.1
 * to offer multiple easing options
 *
 * TERMS OF USE - jQuery Easing
 * 
 * Open source under the BSD License. 
 * 
 * Copyright © 2008 George McGinley Smith
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification, 
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice, this list of 
 * conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list 
 * of conditions and the following disclaimer in the documentation and/or other materials 
 * provided with the distribution.
 * 
 * Neither the name of the author nor the names of contributors may be used to endorse 
 * or promote products derived from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED 
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED 
 * OF THE POSSIBILITY OF SUCH DAMAGE. 
 *
*/

jQuery.easing["jswing"]=jQuery.easing["swing"];jQuery.extend(jQuery.easing,{def:"easeOutQuad",swing:function(e,d,a,b,c){return jQuery.easing[jQuery.easing.def](e,d,a,b,c)},easeInQuad:function(e,a,b,c,d){return c*(a/=d)*a+b},easeOutQuad:function(e,a,b,c,d){return -c*(a/=d)*(a-2)+b},easeInOutQuad:function(e,a,b,c,d){if((a/=d/2)<1)return c/2*a*a+b;return -c/2*(--a*(a-2)-1)+b},easeInCubic:function(e,a,b,c,d){return c*(a/=d)*a*a+b},easeOutCubic:function(e,a,b,c,d){return c*((a=a/d-1)*a*a+1)+b},easeInOutCubic:function(e,a,b,c,d){if((a/=d/2)<1)return c/2*a*a*a+b;return c/2*((a-=2)*a*a+2)+b},easeInQuart:function(e,a,b,c,d){return c*(a/=d)*a*a*a+b},easeOutQuart:function(e,a,b,c,d){return -c*((a=a/d-1)*a*a*a-1)+b},easeInOutQuart:function(e,a,b,c,d){if((a/=d/2)<1)return c/2*a*a*a*a+b;return -c/2*((a-=2)*a*a*a-2)+b},easeInQuint:function(e,a,b,c,d){return c*(a/=d)*a*a*a*a+b},easeOutQuint:function(e,a,b,c,d){return c*((a=a/d-1)*a*a*a*a+1)+b},easeInOutQuint:function(e,a,b,c,d){if((a/=d/2)<1)return c/2*a*a*a*a*a+b;return c/2*((a-=2)*a*a*a*a+2)+b},easeInSine:function(e,d,b,a,c){return -a*Math.cos(d/c*(Math.PI/2))+a+b},easeOutSine:function(e,d,a,b,c){return b*Math.sin(d/c*(Math.PI/2))+a},easeInOutSine:function(e,d,a,b,c){return -b/2*(Math.cos(Math.PI*d/c)-1)+a},easeInExpo:function(e,b,a,c,d){return b==0?a:c*Math.pow(2,10*(b/d-1))+a},easeOutExpo:function(e,d,a,b,c){return d==c?a+b:b*(-Math.pow(2,-10*d/c)+1)+a},easeInOutExpo:function(e,a,b,c,d){if(a==0)return b;if(a==d)return b+c;if((a/=d/2)<1)return c/2*Math.pow(2,10*(a-1))+b;return c/2*(-Math.pow(2,-10*--a)+2)+b},easeInCirc:function(e,a,b,c,d){return -c*(Math.sqrt(1-(a/=d)*a)-1)+b},easeOutCirc:function(e,a,b,c,d){return c*Math.sqrt(1-(a=a/d-1)*a)+b},easeInOutCirc:function(e,a,b,c,d){if((a/=d/2)<1)return -c/2*(Math.sqrt(1-a*a)-1)+b;return c/2*(Math.sqrt(1-(a-=2)*a)+1)+b},easeInElastic:function(h,d,e,a,f){var g=1.70158,b=0,c=a;if(d==0)return e;if((d/=f)==1)return e+a;if(!b)b=f*.3;if(c<Math.abs(a)){c=a;var g=b/4}else var g=b/(2*Math.PI)*Math.asin(a/c);return -(c*Math.pow(2,10*(d-=1))*Math.sin((d*f-g)*(2*Math.PI)/b))+e},easeOutElastic:function(h,d,e,a,f){var g=1.70158,b=0,c=a;if(d==0)return e;if((d/=f)==1)return e+a;if(!b)b=f*.3;if(c<Math.abs(a)){c=a;var g=b/4}else var g=b/(2*Math.PI)*Math.asin(a/c);return c*Math.pow(2,-10*d)*Math.sin((d*f-g)*(2*Math.PI)/b)+a+e},easeInOutElastic:function(h,a,e,b,f){var g=1.70158,c=0,d=b;if(a==0)return e;if((a/=f/2)==2)return e+b;if(!c)c=f*(.3*1.5);if(d<Math.abs(b)){d=b;var g=c/4}else var g=c/(2*Math.PI)*Math.asin(b/d);if(a<1)return -.5*(d*Math.pow(2,10*(a-=1))*Math.sin((a*f-g)*(2*Math.PI)/c))+e;return d*Math.pow(2,-10*(a-=1))*Math.sin((a*f-g)*(2*Math.PI)/c)*.5+b+e},easeInBack:function(f,b,c,d,e,a){if(a==undefined)a=1.70158;return d*(b/=e)*b*((a+1)*b-a)+c},easeOutBack:function(f,b,c,d,e,a){if(a==undefined)a=1.70158;return d*((b=b/e-1)*b*((a+1)*b+a)+1)+c},easeInOutBack:function(f,a,c,d,e,b){if(b==undefined)b=1.70158;if((a/=e/2)<1)return d/2*(a*a*(((b*=1.525)+1)*a-b))+c;return d/2*((a-=2)*a*(((b*=1.525)+1)*a+b)+2)+c},easeInBounce:function(e,d,c,a,b){return a-jQuery.easing.easeOutBounce(e,b-d,0,a,b)+c},easeOutBounce:function(e,a,b,c,d){if((a/=d)<1/2.75)return c*(7.5625*a*a)+b;else if(a<2/2.75)return c*(7.5625*(a-=1.5/2.75)*a+.75)+b;else if(a<2.5/2.75)return c*(7.5625*(a-=2.25/2.75)*a+.9375)+b;else return c*(7.5625*(a-=2.625/2.75)*a+.984375)+b},easeInOutBounce:function(e,c,d,b,a){if(c<a/2)return jQuery.easing.easeInBounce(e,c*2,0,b,a)*.5+d;return jQuery.easing.easeOutBounce(e,c*2-a,0,b,a)*.5+b*.5+d}})