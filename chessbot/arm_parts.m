close all;
figure;

bulx = -0.5;
buly = 0.2;
blrx = 0;
blry = -0.5;
bw = 5;
line([bulx, blrx], [buly, buly],'linewidth',bw);
line([blrx, blrx], [buly, blry],'linewidth',bw);
line([blrx, bulx], [blry, blry],'linewidth',bw);
line([bulx, bulx], [buly, blry],'linewidth',bw);

js = [0.9, -1.3];

l0 = 1.0;
aw = 10; % arm width
elbow_xy = [l0 * cos(js(1)), l0 * sin(js(1))];
line([0,elbow_xy(1)],[0,elbow_xy(2)],'linewidth',aw);
hold on;
l1 = 0.7;
wrist_xy = [elbow_xy(1) + l1 * cos(js(1)+js(2)),
            elbow_xy(2) + l1 * sin(js(1)+js(2))];
line([elbow_xy(1),wrist_xy(1)],
     [elbow_xy(2),wrist_xy(2)],'linewidth',aw);
drawCircle(0, 0, 0.05, 'linewidth', aw, 'k');
drawCircle(elbow_xy(1), elbow_xy(2), 0.05, 'linewidth', aw, 'k');
drawCircle(wrist_xy(1), wrist_xy(2), 0.05, 'linewidth', aw, 'k');

%fs = 32;
text(bulx+0.1, buly-0.2, "immovable\n(grounded)\nbase",'fontsize',32);
text(0.1, -0.05, "joint 0");
text(0.15,  0.5, "link 0");
text(0.9,   0.75, "link 1");
text(elbow_xy(1)-0.05, elbow_xy(2)-0.15, "joint 1");
text(wrist_xy(1)-0.15, wrist_xy(2)-0.15, "end effector");
axis equal;
axis off;
