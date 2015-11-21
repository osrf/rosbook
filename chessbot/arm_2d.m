close all;
% render arm in both poses
function draw_arm(js)
  % fprintf("draw_arm\n");
  % draw the base of the robot
  bulx = -0.5;
  buly = 0.2;
  blrx = 0;
  blry = -1.5;
  bw = 2;
  line([bulx, blrx], [buly, buly],'linewidth',bw);
  line([blrx, blrx], [buly, blry],'linewidth',bw);
  line([blrx, bulx], [blry, blry],'linewidth',bw);
  line([bulx, bulx], [buly, blry],'linewidth',bw);
  fs = 20;
  %text(bulx+0.2, buly-0.2, "cleaner-bot",'fontsize',fs);

  wulx = 1.2;
  wuly = 1.3;
  wlrx = 1.3;
  wlry = -1.1;
  ww = 3;
  line([wulx, wlrx], [wuly, wuly],'linestyle','--','linewidth',ww);
  line([wlrx, wlrx], [wuly, wlry],'linestyle','--','linewidth',bw);
  line([wlrx, wulx], [wlry, wlry],'linestyle','--','linewidth',bw);
  line([wulx, wulx], [wuly, wlry],'linestyle','--','linewidth',bw);


  l0 = 1.0;
  aw = 10; % arm width
  elbow_xy = [l0 * cos(js(1)), l0 * sin(js(1))];
  line([0,elbow_xy(1)],[0,elbow_xy(2)],'linewidth',aw);
  l1 = 0.7;
  wrist_xy = [elbow_xy(1) + l1 * cos(js(1)+js(2)),
              elbow_xy(2) + l1 * sin(js(1)+js(2))];
  line([elbow_xy(1),wrist_xy(1)],
       [elbow_xy(2),wrist_xy(2)],'linewidth',aw);
endfunction

js_start = [ 0.9, -0.3];
js_end   = [-1,  0.7];
figure;
for t=0:0.10:1
  draw_arm(js_start * (1-t) + js_end * t);
end
axis equal;
